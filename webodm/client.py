import requests

from .exceptions import NonFieldErrors

LOCAL_HOST = 'http://localhost:8000'


class Webodm(object):

    def __init__(self, username=None, password=None, host=LOCAL_HOST):
        if username is not None and password is None:
            AttributeError('Username passed, but password is missing.')
        elif username is None and password is not None:
            AttributeError('Password passed, but username is missing.')

        self.token = None
        self.host = host

        if username is not None and password is not None:
            self.authenticate(username, password)

    def authenticate(self, username, password):
        url = '{}{}'.format(self.host, '/api/token-auth/')
        req_data = {
            'username': username,
            'password': password
        }
        resp = requests.post(url, data=req_data)

        data = resp.json()
        if resp.status_code == 400 and 'non_field_errors' in data:
            errors = " ".join(data.get('non_field_errors'))
            raise NonFieldErrors(errors, response=resp)

        self.token = data.get('token')
