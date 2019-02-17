from base64 import b64encode
from requests import post


class Client:
    BASE_URL = 'https://hsp-prod.rockshore.net/api/v1'

    def __init__(self, email: str, password: str, base_url: str = None):
        self.email = email
        self.password = password
        self.base_url = base_url if base_url else Client.BASE_URL

    def _make_request(self, endpoint, json):
        headers = {
            'Accept': 'application/json',
            'Authorization': "Basic " + b64encode(f"{self.email}:{self.password}".encode()).decode(),
            'Content-Type': 'application/json'
        }

        r = post(f'{self.base_url}/{endpoint}', headers=headers, json=json)
        return r.json()

    def get_service_metrics(self):
        return self._make_request('serviceMetrics', {})

    def get_service_details(self, rid):
        return self._make_request('serviceDetails', {'rid': rid})
