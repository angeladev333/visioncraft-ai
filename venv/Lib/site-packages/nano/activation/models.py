from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
import django.dispatch
from django.conf import settings
from django.db import models
from django.utils.timezone import now as tznow

from nano.activation.signals import key_activated

Q = models.Q

class ActivationError(Exception):
    pass

class ActivationKeyError(ActivationError):
    pass

def activate(keystring, user):
    """Attempts to activate a specific key for user, returns activated key on activation,
    raises an exception otherwise"""
    try:
        key = Key.objects.get(key=keystring)
    except Key.DoesNotExist:
        raise ActivationKeyError('Key %s does not exist, typo?' % keystring)
    key.activate(user)
    return key

class KeyManager(models.Manager):

    def expired(self):
        now = tznow()
        return self.get_queryset().exclude(expires=None).filter(expires__lte=now)

    def available(self):
        now = tznow()
        return self.get_queryset().filter(Q(expires__gt=now)|Q(expires=None)).filter(activated=None)

    def activated(self):
        now = tznow()
        return self.get_queryset().exclude(activated=None)

    def activate(self, *args):
        return activate(*args)

@python_2_unicode_compatible
class Key(models.Model):
    key = models.CharField(max_length=255)
    group = models.SlugField(max_length=32, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    expires = models.DateTimeField(blank=True, null=True)
    activated = models.DateTimeField(blank=True, null=True)
    activated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='activation_keys'
    )

    objects = KeyManager()

    class Meta:
        db_table = 'nano_activation_code'
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'

    def __str__(self):
        pp_pub_date = self.pub_date
        pp_expires = self.expires or ''
        return "%s (%s) %s %s" % (self.key, self.group, pp_pub_date, pp_expires)

    def activate(self, user):
        """Activates a specific key for user, returns activated key on activation,
        raises an exception otherwise"""
        now = tznow()
        if self.expires and self.expires <= now:
            raise ActivationKeyError('Key expired on %s' % self.expires)
        if self.activated:
            raise ActivationKeyError('Key has already been activated')
        self.activated_by = user
        self.activated = now
        self.save()
        key_activated.send_robust(sender=self, user=user, group=self.group)
        return self
