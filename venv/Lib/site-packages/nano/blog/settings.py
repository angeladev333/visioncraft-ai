from django.conf import settings

NANO_BLOG_TAGS = None

# Optional support for django-taggit
try:
    if ('taggit' in settings.INSTALLED_APPS 
        and getattr(settings, 'NANO_BLOG_USE_TAGS', False)):
        import taggit as NANO_BLOG_TAGS
except ImportError:
    pass

NANO_BLOG_SPECIAL_TAGS = getattr(settings, 'NANO_BLOG_SPECIAL_TAGS', ('pinned',))
