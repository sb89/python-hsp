class Client:
    BASE_URL = 'https://hsp-prod.rockshore.net/api/v1'

    def __init__(self, email: str, password: str, base_url: str = None):
        self.email = email
        self.password = password
        self.base_url = base_url if base_url else Client.BASE_URL


