from django.test import TestCase, Client
from .models import City, Walk


# Create your tests here.


class ViewTest (TestCase):
    def setUp(self):
        self.client = Client()

    def test_main_page(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_walk_page(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)


class BDTest (TestCase):
    def setUp(self):
        City.objects.create(name='Москва')
        City.objects.create(name='Волгоград')

    def test_city(self):
        cities = City.objects.all()
        self.assertEqual(len(cities), 2)

