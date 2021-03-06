# encoding: utf-8


class RequestException(Exception):
    def __init__(self, status_code=500, content=None):
        message = "Status: {}. Problem with the request exiting.".format(
            status_code)
        self.status_code = status_code
        self.content = content
        super(RequestException, self).__init__(message)


class BulkExceededLimit(Exception):
    def __init__(self):
        message = "The bulk can not exceed 100 objects"
        super(BulkExceededLimit, self).__init__(message)


class TooManyRequestsException(Exception):
    def __init__(self, content=None, retry_after=60):
        message = "Too many Requests were made in the same time slice, \
try again after {} seconds.".format(retry_after)
        self.content = content
        self.retry_after = retry_after
        super(TooManyRequestsException, self).__init__(message)
