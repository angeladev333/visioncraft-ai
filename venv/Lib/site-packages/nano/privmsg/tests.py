from __future__ import unicode_literals

from django.test import TestCase

from nano.privmsg.models import PM

from django.contrib.auth import get_user_model

class PMTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.sender = User.objects.create(username='Sender')
        self.recipient = User.objects.create(username='Recipient')

    def test_str(self):
        item = PM(subject='test', text='Test')
        self.assertEqual(str(item), 'test')
        test_content = '0123456789'*10
        item = PM(text=test_content)
        self.assertTrue(len(str(item)) <= 64)
        self.assertEqual(str(item), test_content[:64])

    def test_save(self):
        test_content = '0123456789'*10
        item = PM(text=test_content, sender=self.sender, recipient=self.recipient)
        item.save()
        self.assertEqual(item.subject, test_content[:63]+'\u2026')

    def test_is_deleted(self):
        item = PM.objects.create(text='test', sender=self.sender, recipient=self.recipient)
        self.assertFalse(item.is_deleted())
        item.sender_deleted = True
        self.assertFalse(item.is_deleted())
        item.recipient_deleted = True
        self.assertTrue(item.is_deleted())

    def test_delete(self):
        item = PM.objects.create(text='test', sender=self.sender, recipient=self.recipient)
        item.delete()
        try:
            item = PM.objects.get(text='test')
        except PM.DoesNotExist:
            self.fail('PM deleted even though not marked for deletion')
        item.sender_deleted = True
        item.recipient_deleted = True
        item.delete()
        try:
            item = PM.objects.get(text='test')
            self.fail('PM not deleted even though marked for deletion')
        except PM.DoesNotExist:
            pass
