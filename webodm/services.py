#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""API Services used by the Client."""

import requests

from .exceptions import NonFieldErrors, ImproperlyConfigured


class Service(object):

    def __init__(self, host, token=None):
        self.host = host
        self.token = token

    def get_endpoint(self):
        if self.endpoint:
            return self.endpoint
        else:
            raise ImproperlyConfigured(
                    "No endpoint configured."
                    " Provide an endpoint.")

    def get_auth_header(self):
        if self.token is not None:
            return {'Authorization': 'JWT {0}'.format(self.token)}
        else:
            raise ImproperlyConfigured(
                    "No token configured."
                    " Pass a token to the Service contructor.")


class AuthService(Service):
    endpoint = '/api/token-auth/'

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


class ProjectsService(Service):
    endpoint = '/api/projects/'

    def create(self, name, description=None):
        url = '{0}{1}'.format(self.host, self.endpoint)
        params = {
            'name': name,
            'description': description
        }

        resp = requests.post(url, headers=self.get_auth_header(), data=params)

        return resp.json()

    def update(self, project_id, name, description=None):
        url = '{0}{1}{2}/'.format(self.host, self.endpoint, project_id)
        params = {
            'name': name,
            'description': description
        }

        resp = requests.patch(url, headers=self.get_auth_header(), data=params)
        data = resp.json()

        if resp.status_code >= 400 and resp.status_code < 500:
            errors = " ".join(data.values())
            error_msg = "{0} - {1}".format(resp.status_code, errors)
            raise requests.HTTPError(error_msg, response=resp)

        return data

    def delete(self, project_id):
        url = '{0}{1}{2}/'.format(self.host, self.endpoint, project_id)
        resp = requests.delete(url, headers=self.get_auth_header())

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
        resp = requests.get(url, headers=self.get_auth_header())
        data = resp.json()

        if resp.status_code >= 400 and resp.status_code < 500:
            errors = " ".join(data.values())
            error_msg = "{0} - {1}".format(resp.status_code, errors)
            raise requests.HTTPError(error_msg, response=resp)

        return data

    def list(self):
        url = '{0}{1}'.format(self.host, self.endpoint)
        resp = requests.get(url, headers=self.get_auth_header())
        data = resp.json()

        if resp.status_code >= 400 and resp.status_code < 500:
            errors = " ".join(data.values())
            error_msg = "{0} - {1}".format(resp.status_code, errors)
            raise requests.HTTPError(error_msg, response=resp)

        return data
