class ResponseException(Exception):
    def __init__(self, msg, response):
        self.msg = msg
        self.response = response

    def __str__(self):
        return repr(self.msg)
