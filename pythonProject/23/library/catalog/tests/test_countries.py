from django.test import TestCase
from catalog.models import Country


class CountryStrTestCase(TestCase):

    def setUp(self) -> None:
        Country.objects.create(name='Bangladesh')

    def test_str_representation(self):
        country = Country.objects.get(id=1)
        self.assertEquals(country.name, str(country))