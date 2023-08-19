from __future__ import unicode_literals

from django.test import TestCase

from nano.faq.models import QA
from nano.faq.views import ListFAQView

class QATest(TestCase):

    def test_str(self):
        item = QA(question='blbl', answer='fofo')
        self.assertEqual(str(item), item.question)

    def test_save(self):
        item = QA(question='blbl', answer='fofo')
        item.save()
        self.assertNotEqual(item.last_modified, None)

class ListFAQViewTest(TestCase):

    def test_get_context_data(self):
        view = ListFAQView()
        view.object_list = None
        context = view.get_context_data(object_list=None)
        self.assertEqual(context['me'], 'faq')
