from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class Chunk(models.Model):
    slug = models.SlugField()
    content = models.TextField()

    class Meta:
        db_table = 'nano_chunk_chunk'

    def __str__(self):
        return self.slug
    
