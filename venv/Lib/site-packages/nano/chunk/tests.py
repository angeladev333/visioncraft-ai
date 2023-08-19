from __future__ import unicode_literals

from django.test import TestCase
from django.template.engine import Engine
from django.template import TemplateDoesNotExist

from nano.chunk.models import Chunk


class ChunkTest(TestCase):

    def setUp(self):
        engine = Engine(loaders=['nano.chunk.loaders.ChunkLoader'])
        self.loader = engine.template_loaders[0]

    def test_str(self):
        item = Chunk(slug='test', content='Test')
        self.assertEqual(str(item), item.slug)

    def test_non_existing(self):
        with self.assertRaises(TemplateDoesNotExist):
            self.loader.load_template_source("not-existing.html")

    def test_existing(self):
        content = 'Test!'
        template_name = 'test'
        chunk = Chunk.objects.create(slug=template_name, content=content)
        result = self.loader.load_template_source("test")
        self.assertEqual(result[0], content)
        self.assertEqual(result[1], template_name)
