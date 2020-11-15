class LoginAttemptFailed(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.message = "Login attempt is failed"
        self.status_code = 401

    def to_dict(self):
        return dict({'message': self.message, 'status': self.status_code})
