import django.dispatch

default_app_config = 'nano.user.apps.NanoUserConfig'

new_user_created = django.dispatch.Signal(providing_args=['user'])
