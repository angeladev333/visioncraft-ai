from django.conf import settings

default_app_config = 'nano.comments.apps.NanoCommentsConfig'

COMMENT_MAX_LENGTH = getattr(settings,'COMMENT_MAX_LENGTH',3000)
