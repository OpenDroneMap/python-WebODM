import requests

from .exceptions import NonFieldErrors

LOCAL_HOST = 'http://localhost:8000'


class Webodm(object):

    def __init__(self, username=None, password=None, host=LOCAL_HOST):
        self.token = None
        self.host = host
        
        if username is not None and password is None:
            AttributeError('Username passed, but password is missing.')
        elif username is None and password is not None:
            AttributeError('Password passed, but username is missing.')

        if username is not None and password is not None:
            self.authenticate(username, password)

    def authenticate(self, username, password):
        resp = requests.post(
            '{}{}'.format(self.host, '/api/token-auth/'),
            data={
                'username': username,
                'password': password
            })

        data = resp.json()
        if resp.status_code == 400:
            if 'non_field_errors' in data:
                errors = " ".join(data.get('non_field_errors'))
                raise NonFieldErrors(errors, response=resp)

        self.token = data.get('token')
