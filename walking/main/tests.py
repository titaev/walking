from django.test import TestCase, Client
from .models import City


class ViewTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        # self.assertEqual(len(response.context['customers']), 5)

class BDTest(TestCase):
    def setUp(self):
        City.objects.create(name="Москва")
        City.objects.create(name="Санкт-Петербург")

    def test_city(self):
        cities = City.objects.all()
        self.assertEqual(len(cities), 2)




