
# Create your tests here.
from django.test import TestCase, Client


class ViewTest (TestCase):
    def setUp(self):
        self.client = Client()

    def test_main_page(self):
        resp = self.client.get('/accounts/login/')
        self.assertEqual(resp.status_code, 200)

    def test_register_page(self):
        resp = self.client.get('/accounts/register/')
        self.assertEqual(resp.status_code, 200)

