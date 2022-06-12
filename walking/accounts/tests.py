from django.test import TestCase, Client


class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_page(self):
        resp = self.client.get('/accounts/login/')
        self.assertEqual(resp.status_code, 200)  # при замене на 300 выдает ошибку с подробным описанием

    def test_register_page(self):
        resp = self.client.get('/accounts/register/')
        self.assertEqual(resp.status_code, 200)
