"""
Wrapper for loading templates from the filesystem.
"""

from django.apps import apps
from django.conf import settings
from django.template import TemplateDoesNotExist
from django.utils._os import safe_join

from django.template.loaders.base import Loader

class ChunkLoader(Loader):
    is_usable = True

    def load_template_source(self, template_name, template_dirs=None):
        chunk_model = apps.get_model('chunk', 'Chunk')
        try:
            chunk = chunk_model.objects.get(slug=template_name)
            return (chunk.content, template_name)
        except chunk_model.DoesNotExist:
            error_msg = "Couldn't find a chunk named %s" % template_name
            raise TemplateDoesNotExist(error_msg)
