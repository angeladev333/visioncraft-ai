from django.conf.urls import url
from django.shortcuts import render

from nano.activation.views import activate_key


urlpatterns = [
    url(r'^activate$',       activate_key, name='nano-activate-key'),
    url(r'^activation_ok/$', render,
                             {'template_name': 'nano/activation/activated.html'},
                             name='nano-activation-ok'),
]
