import unittest
import responses
from base64 import b64encode

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

    @responses.activate
    def test_client_request_sets_accept_header(self):
        responses.add(responses.POST, 'https://hsp-prod.rockshore.net/api/v1/serviceDetails', json={}, status=200)

        client = Client(self.email, self.password)
        client.get_service_details()

        self.assertEqual(responses.calls[0].request.headers.get('Accept'), 'application/json')

    @responses.activate
    def test_client_request_sets_content_type_header(self):
        responses.add(responses.POST, 'https://hsp-prod.rockshore.net/api/v1/serviceDetails', json={}, status=200)

        client = Client(self.email, self.password)
        client.get_service_details()

        self.assertEqual(responses.calls[0].request.headers.get('Content-Type'), 'application/json')

    @responses.activate
    def test_client_request_sets_authorization_header(self):
        responses.add(responses.POST, 'https://hsp-prod.rockshore.net/api/v1/serviceDetails', json={}, status=200)

        client = Client(self.email, self.password)
        client.get_service_details()

        expected_value = b64encode(f"{self.email}:{self.password}".encode())

        self.assertEqual(responses.calls[0].request.headers.get('Authorization'), expected_value)
