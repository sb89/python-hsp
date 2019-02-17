from base64 import b64encode
from http.client import responses
from requests import post, Response
from typing import Dict

from hsp.exception import HSPException


class Client:
    BASE_URL = 'https://hsp-prod.rockshore.net/api/v1'

    def __init__(self, email: str, password: str, base_url: str = None):
        self.email = email
        self.password = password
        self.base_url = base_url if base_url else Client.BASE_URL

    def _make_request(self, endpoint: str, json: Dict[str, str]):
        headers = {
            'Accept': 'application/json',
            'Authorization': "Basic " + b64encode(f"{self.email}:{self.password}".encode()).decode(),
            'Content-Type': 'application/json'
        }

        r = post(f'{self.base_url}/{endpoint}', headers=headers, json=json)
        self._raise_for_error(r)

        return r.json()

    def _raise_for_error(self, resp: Response):
        if resp.status_code == 200:
            return

        status = responses[resp.status_code]
        errors = []
        if resp.headers.get('Content-Type') == 'application/json;charset=UTF-8':
            errors = resp.json()['my_journey_errors']['errors']

        raise HSPException(status, errors=errors)

    def get_service_metrics(self, data: Dict[str, str]):
        return self._make_request('serviceMetrics', data)

    def get_service_details(self, rid: str):
        return self._make_request('serviceDetails', {'rid': rid})
