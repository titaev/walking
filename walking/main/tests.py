from django.test import TestCase, Client
from .models import City, Walk

class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_main_page(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)  # при замене на 300 выдает ошибку с подробным описанием


class BDTest(TestCase):
    def setUp(self):
        City.objects.create(name='New-Yourk')
        City.objects.create(name='Los-Angeles')

    def test_city(self):
        cities = City.objects.all()
        self.assertEqual(len(cities), 2)  # при замене на 3 выдает ошибку с подробным описанием

