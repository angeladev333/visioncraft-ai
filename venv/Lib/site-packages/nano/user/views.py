from __future__ import unicode_literals

from random import choice, sample
import string

from django.utils.timezone import now as tznow
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template.defaultfilters import slugify
try:
    from django.urls import reverse
except ImportError:  # Django < 1.10
    from django.core.urlresolvers import reverse

from nano.tools import pop_error, get_profile_model, asciify
from nano.user.forms import SignupForm, PasswordChangeForm, PasswordResetForm
from nano.user import new_user_created


import logging
_LOG = logging.getLogger(__name__)

class NanoUserError(Exception):
    pass

class NanoUserExistsError(NanoUserError):
    pass

# def pop_error(request):
#     error = request.session.get('error', None)
#     if 'error' in request.session:
#         del request.session['error']
#     return error

def random_password():
    sample_space = string.ascii_letters + string.digits + r'!#$%&()*+,-.:;=?_'
    outlist = []
    for i in range(1,8):
        chars = sample(sample_space, 2)
        outlist.extend(chars)
    return ''.join(outlist)

def make_user(username, password, email=None, request=None):
    User = get_user_model()
    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
        # make user
        user = User(username=username[:30])
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.is_active = True
        if email:
            user.email = email
        user.save()
        
        # Create profile
        Profile = get_profile_model(raise_on_error=False)
        if Profile:
            profile = Profile(user=user, display_name=username)
            profile.save()

        # Don't signal creation of test users
        test_users = getattr(settings, 'NANO_USER_TEST_USERS', ())
        for test_user in test_users:
            if user.username.startswith(test_user):
                break
        else:
            new_user_created.send(sender=User, user=user) 
        if request is not None:
            infomsg = 'You\'re now registered, as "%s"' % username
            messages.info(request, infomsg)
            _LOG.debug('Created user: %s/%s' % (user, user.check_password(password)))
        return user
    else:
        raise NanoUserExistsError("The username '%s' is already in use by somebody else" % username)

def signup(request, template_name='signup.html', *args, **kwargs):
    me = 'people'
    error = pop_error(request)
    data = {
            'me': me, 
            'error': error, 
            'form': SignupForm()
    }
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            username = asciify(form.cleaned_data['username'])
            password = form.cleaned_data['password2']
            email = form.cleaned_data['email'].strip() or ''

            errormsg = 'Username "%s" is taken'

            # check that username not taken
            userslug = slugify(username)
            Profile = get_profile_model(raise_on_error=False)
            if Profile.objects.filter(slug=userslug).count():
                # error!
                safe_username = slugify('%s-%s' % (username, str(tznow())))
                changed_warningmsg = errormsg + ", changed it to '%s'."
                messages.warning(request, changed_warningmsg % (username, safe_username))
                username = safe_username

            # make user
            try:
                user = make_user(username, password, email=email, request=request)
            except NanoUserExistsError:
                next_profile = Profile.objects.get(user=user).get_absolute_url()
                return HttpResponseRedirect(next_profile)
            else:
                # fake authentication, avoid a db-lookup/thread-trouble/
                # race conditions
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                _LOG.debug('Attempting login of: %s' % user)
                login(request, user)
                nexthop = getattr(settings, 'NANO_USER_SIGNUP_NEXT', reverse('nano_user_signup_done'))
                try:
                    nexthop_profile = Profile.objects.get(user=user).get_absolute_url()
                    return HttpResponseRedirect(nexthop_profile)
                except Profile.DoesNotExist:
                    pass
                return HttpResponseRedirect(nexthop)
            _LOG.debug('Should never end up here')
    return render(request, template_name, data)

@login_required
def password_change(request, *args, **kwargs):
    error = pop_error(request)
    template_name = 'password_change_form.html'
    if request.method == "POST":
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password2']
            user = request.user
            user.set_password(password)
            user.save()
            request.session['error'] = None
            return HttpResponseRedirect('/password/change/done/')
    else:
        form = PasswordChangeForm()
    data = { 'form': form,
            'error': error,}
    return render(request, template_name, data)

def password_reset(request, project_name='Nano', *args, **kwargs):
    User = get_user_model()
    error = pop_error(request)
    template = 'password_reset_form.html'
    e_template = 'password_reset.txt'
    help_message = None
    e_subject = '%s password assistance' % project_name
    e_message = """Your new password is: 

%%s

It is long deliberately, so change it to 
something you'll be able to remember.


%s' little password-bot
""" % project_name
    e_from = getattr(settings, 'NANO_USER_EMAIL_SENDER', '')
    form = PasswordResetForm()
    if e_from and request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user = get_object_or_404(User, username=form.cleaned_data['username'])
            if user.email:
                tmp_pwd = random_password()
                user.set_password(tmp_pwd)
                result = send_mail(subject=e_subject, from_email=e_from, message=e_message % tmp_pwd, recipient_list=(user.email,))
                user.save()
                request.session['error'] = None
                return HttpResponseRedirect('/password/reset/sent/')
            else:
                error = """There's no email-address registered for '%s', 
                        the password can't be reset.""" % user.username
                request.session['error'] = error
                
    data = {'form': form,
            'help_message': help_message,
            'error':error}
    return render(request, template, data)

