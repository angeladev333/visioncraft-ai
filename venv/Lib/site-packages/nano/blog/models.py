from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from nano.blog.settings import NANO_BLOG_TAGS

# Optional support for django-taggit
# For some unfathomable reason this cannot be imported inside the class
# as of Django 1.3
if NANO_BLOG_TAGS:
    from taggit.managers import TaggableManager

@python_2_unicode_compatible
class Entry(models.Model):
    headline = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateTimeField()

    # Optional support for django-taggit
    if NANO_BLOG_TAGS:
        tags = TaggableManager(blank=True)

    class Meta:
        db_table = 'nano_blog_entry'
        verbose_name_plural = 'entries'
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'

    def __str__(self):
        return self.headline
