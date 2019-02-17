import unittest

from hsp.client import Client


class TestClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.email = 'example@example.com'
        cls.password = 'password'

    def test_client_sets_base_url_to_default(self):
        c = Client(self.email, self.password)

        self.assertEqual(c.base_url, Client.BASE_URL)

    def test_client_uses_specified_base_url(self):
        base_url = 'This is the custom base url'

        c = Client(self.email, self.password, base_url)

        self.assertEqual(c.base_url, base_url)
