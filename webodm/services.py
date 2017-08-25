#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""API Services used by the Client."""

import requests

from .exceptions import NonFieldErrors


class AuthService(object):
    endpoint = '/api/token-auth/'

    def __init__(self, host):
        self.host = host

    def auth(self, username, password):
        url = '{0}{1}'.format(self.host, self.endpoint)
        req_data = {
            'username': username,
            'password': password
        }
        resp = requests.post(url, data=req_data)
        data = resp.json()

        # Throw Exception when response has 'non_field_errors'
        if resp.status_code == 400 and 'non_field_errors' in data:
            errors = data.get('non_field_errors')
            raise NonFieldErrors(errors, response=resp)

        return data.get('token')


class ProjectsService(object):
    endpoint = '/api/projects/'

    def __init__(self, host, token=None):
        self.token = token
        self.host = host

    def create(self, name, description=None):
        url = '{0}{1}'.format(self.host, self.endpoint)
        auth_header = {'Authorization': 'JWT {0}'.format(self.token)}
        data = {
            'name': name,
            'description': description
        }

        resp = requests.post(url, headers=auth_header, data=data)
        return resp.json()

    def update(self, project_id, name, description=None):
        url = '{0}{1}{2}/'.format(self.host, self.endpoint, project_id)
        auth_header = {'Authorization': 'JWT {0}'.format(self.token)}
        data = {
            'name': name,
            'description': description
        }

        resp = requests.patch(url, headers=auth_header, data=data)
        data = resp.json()

        if resp.status_code >= 400 and resp.status_code < 500:
            errors = " ".join(data.values())
            error_msg = "{0} - {1}".format(resp.status_code, errors)
            raise requests.HTTPError(error_msg, response=resp)

        return data

    def delete(self, project_id):
        url = '{0}{1}{2}/'.format(self.host, self.endpoint, project_id)
        auth_header = {'Authorization': 'JWT {0}'.format(self.token)}

        resp = requests.delete(url, headers=auth_header)

        if resp.status_code >= 400 and resp.status_code < 500:
            data = resp.json()
            errors = " ".join(data.values())
            error_msg = "{0} - {1}".format(resp.status_code, errors)
            raise requests.HTTPError(error_msg, response=resp)
        elif resp.status_code == 204:
            return True

        raise Exception('Unexpected status code: {0}'.format(resp.status_code))

    def get(self, project_id):
        url = '{0}{1}{2}/'.format(self.host, self.endpoint, project_id)
        auth_header = {'Authorization': 'JWT {0}'.format(self.token)}
        resp = requests.get(url, headers=auth_header)
        data = resp.json()

        if resp.status_code >= 400 and resp.status_code < 500:
            errors = " ".join(data.values())
            error_msg = "{0} - {1}".format(resp.status_code, errors)
            raise requests.HTTPError(error_msg, response=resp)

        return data

    def list(self):
        url = '{0}{1}'.format(self.host, self.endpoint)
        auth_header = {'Authorization': 'JWT {0}'.format(self.token)}
        resp = requests.get(url, headers=auth_header)
        data = resp.json()

        if resp.status_code >= 400 and resp.status_code < 500:
            errors = " ".join(data.values())
            error_msg = "{0} - {1}".format(resp.status_code, errors)
            raise requests.HTTPError(error_msg, response=resp)

        return data
