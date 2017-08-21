import requests

from exceptions import NonFieldErrors

LOCAL_HOST = 'http://localhost:8000'


class Webodm(object):

    def __init__(self, username, password, host=LOCAL_HOST):
        self.host = host
        self.token = self.get_token(username, password)

    def get_token(self, username, password):
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

        return data.get('token')
