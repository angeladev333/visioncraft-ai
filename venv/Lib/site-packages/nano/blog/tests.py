from __future__ import unicode_literals

from datetime import datetime

from django.test import TestCase
from django.utils import six

from nano.blog.models import Entry
from nano.blog.views import ListBlogView

class BlogMixinTest(TestCase):

    def test_get_context_data(self):
        view = ListBlogView()
        view.object_list = None
        context = view.get_context_data(object_list=None)
        self.assertEqual(context['me'], 'news')

class EntryTest(TestCase):

    def test_str(self):
        pub_date = datetime(2014, 4, 1, 0)
        e = Entry(headline='test', content='test content', pub_date=pub_date)
        e.save()
        self.assertEqual('test', six.text_type(e))
