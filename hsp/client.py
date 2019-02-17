from base64 import b64encode
from requests import post


class Client:
    BASE_URL = 'https://hsp-prod.rockshore.net/api/v1'

    def __init__(self, email: str, password: str, base_url: str = None):
        self.email = email
        self.password = password
        self.base_url = base_url if base_url else Client.BASE_URL

    def _make_request(self, endpoint):
        headers = {
            'Accept': 'application/json',
            'Authorization': b64encode(f"{self.email}:{self.password}".encode()),
            'Content-Type': 'application/json'
        }

        r = post(f'{self.base_url}/{endpoint}', headers=headers)

        return r.json()

    def get_service_metrics(self):
        pass

    def get_service_details(self):
        return self._make_request('serviceDetails')
