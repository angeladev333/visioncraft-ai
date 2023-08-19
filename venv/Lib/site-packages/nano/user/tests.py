from django.utils.timezone import now as tznow
from django.test import TestCase

from nano.faq.models import QA

class QATest(TestCase):

    def test_str(self):
        item = QA(question='blbl', answer='fofo')
        self.assertEqual(str(item), item.question)

    def test_save(self):
        item = QA(question='blbl', answer='fofo')
        item.save()
        self.assertNotEqual(item.last_modified, None)
