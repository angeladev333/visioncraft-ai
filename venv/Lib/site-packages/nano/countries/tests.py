from django.test import TestCase

from nano.countries.models import Country

class CountryTest(TestCase):

    def test_str(self):
        item = Country(iso='no', name='Norway')
        self.assertEqual(str(item), item.name)

    def test_printable_name(self):
        item = Country(iso='no', name='Norway')
        self.assertEqual(item.printable_name, item.name)
