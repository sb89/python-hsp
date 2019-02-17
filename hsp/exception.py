from typing import List


class HSPException(Exception):
    def __init__(self, message: str, errors: List[str] = None):
        self.errors = errors or []

        super().__init__(message)
