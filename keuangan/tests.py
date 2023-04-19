from django.test import TestCase
from keuangan.models import Product
# Create your tests here.
class AnimalTestCase(TestCase):
    def setUp(self):
        Product.objects.create(nama="lion")
        Product.objects.create(nama="cat")

    def test_animals_can_speak(self):
        lion = Product.objects.get(nama="lion")
        cat = Product.objects.get(nama="cat")
        self.assertEqual(lion.nama, 'lion')
        self.assertEqual(cat.nama, 'cat')