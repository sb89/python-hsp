class HSPException(Exception):
    def __init__(self, message, errors=None):
        self.errors = errors or []

        super().__init__(message)
