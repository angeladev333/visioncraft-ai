from __future__ import unicode_literals

from unittest import TestCase as LightTestCase
from datetime import timedelta

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils.timezone import now as tznow

from nano.activation.models import activate, Key, ActivationKeyError
from nano.activation import to_base, NUMERALS, generate_keys, baseNgenerator

class KeyTest(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create(username='test')

    def test_str(self):
        item = Key.objects.create(key='test')
        pub_date = item.pub_date
        expected = "test (None) %s %s" % (pub_date, '')
        self.assertEqual(str(item), expected)

    def test_activate_method(self):
        item = Key.objects.create(key='test')
        item.activate(self.user)
        self.assertIsNotNone(item.activated)

    def test_activate_method_already_activated(self):
        item = Key.objects.create(key='test')
        item.activate(self.user)
        with self.assertRaises(ActivationKeyError) as error:
            item.activate(self.user)
            self.assertEqual(error, 'Key has already been activated')

    def test_activate_function(self):
        with self.assertRaises(ActivationKeyError) as error:
            activate('foo', self.user)
            self.assertEqual(error, 'Key foo does not exist, typo?')
        item = Key.objects.create(key='bar')
        item = activate(item.key, self.user)
        self.assertIsNotNone(item.activated)

    def test_activate_expired_key(self):
        now = tznow()
        item = Key(key='test', expires=now)
        with self.assertRaises(ActivationKeyError) as error:
            item.activate(self.user)
            self.assertEqual(error, 'Key expired on %s' % item.expires)

class KeyManagerTest(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create(username='test')
        self.keys = []
        for i in range(10):
            key = Key.objects.create(key=str(i))
            self.keys.append(key)

    def test_get_all_keys(self):
        result1 = Key.objects.order_by('id')
        self.assertEqual(self.keys, list(result1))
        result2 = Key.objects.available().order_by('id')
        self.assertEqual(self.keys, list(result2))
        self.assertEqual(list(result1), list(result2))

    def test_get_expired_keys(self):
        now = tznow() - timedelta(days=1)
        for key in self.keys[5:]:
            key.expires = now
            key.save()
        self.assertEqual(
            list(Key.objects.expired().order_by('id')), 
            self.keys[5:]
        )
        self.assertEqual(
            list(Key.objects.available().order_by('id')), 
            self.keys[:5]
        )

    def test_get_activated_keys(self):
        now = tznow()
        for key in self.keys[5:]:
            key.activated = now
            key.save()
        self.assertEqual(
            list(Key.objects.activated().order_by('id')), 
            self.keys[5:]
        )
        self.assertEqual(
            list(Key.objects.available().order_by('id')), 
            self.keys[:5]
        )

    def test_activate_keys(self):
        now = tznow() - timedelta(days=1)
        for i in range(5):
            Key.objects.activate(str(i), self.user)
        self.assertEqual(
            list(Key.objects.activated().order_by('id')), 
            self.keys[:5]
        )
        self.assertEqual(
            list(Key.objects.available().order_by('id')), 
            self.keys[5:]
        )
        # Expired key
        self.keys[-1].expires = now
        self.keys[-1].save()
        with self.assertRaises(ActivationKeyError) as error:
            Key.objects.activate(self.keys[-1].key, self.user)
            self.assertEqual(error, 'Key expired on %s' % now)
        # Activated key
        with self.assertRaises(ActivationKeyError) as error:
            Key.objects.activate(self.keys[0].key, self.user)
            self.assertEqual(error, 'Key has already been activated')

class FunctionTest(LightTestCase):
    
    def test_to_base(self):
        # must succeed
        result, expected = to_base(0, 20), '0'
        self.assertEqual(result, expected)
        result, expected = to_base(7, 1), '1'*7
        self.assertEqual(result, expected)
        result, expected = to_base(7, 5), '12'
        self.assertEqual(result, expected)
        result, expected = to_base(-7, 5), '-12'
        self.assertEqual(result, expected)

        # must fail
        with self.assertRaises(ValueError) as error:
            maxbase = len(NUMERALS)
            result, expected = to_base(7, maxbase+1)
            self.assertEqual(error, "<base> must be in the range [1, %i>" % maxbase)
        with self.assertRaises(ValueError) as error:
            result, expected = to_base('q', 10)
            self.assertEqual(error, 'invalid literal for int() with base 10: \'q\'')
        with self.assertRaises(ValueError) as error:
            result, expected = to_base(1, 'q')
            self.assertEqual(error, 'invalid literal for int() with base 10: \'q\'')

    def test_generate_keys(self):
        amount = 10
        result = generate_keys(baseNgenerator(), amount=amount)
        self.assertEqual(amount, len(set(result)))
