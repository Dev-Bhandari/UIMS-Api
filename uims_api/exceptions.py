class IncorrectCredentialsError(Exception):
    def __init__(self, message=None):
        super(IncorrectCredentialsError, self).__init__(message)

class IncorrectCaptcha(Exception):
    def __init__(self, message=None):
        super(IncorrectCaptcha, self).__init__(message)

class UIMSInternalError(Exception):
    def __init__(self, message=None):
        super(UIMSInternalError, self).__init__(message)
