#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""API Services used by the Client."""

import requests

from .exceptions import NonFieldErrors, ImproperlyConfigured
from .models import Project, as_project_list, as_task_list


class Service(object):
    def __init__(self, host, token=None):
        self.host = host
        self.token = token

    def get_auth_header(self):
        if self.token is not None:
            return {'Authorization': 'JWT {0}'.format(self.token)}
        else:
            raise ImproperlyConfigured(
                "No token configured."
                " Pass a token to the Service contructor or set it's value.")


class AuthService(Service):

    def auth(self, username, password):
        url = '{0}/api/token-auth/'.format(self.host)
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

        self.token = data.get('token')
        return data.get('token')


class ProjectsService(Service):
    def get_endpoint(self):
        return '/api/projects/'

    @property
    def general_url(self):
        return '{0}{1}'.format(self.host, self.get_endpoint())

    def specific_url(self, project_id):
        return '{0}{1}{2}/'.format(self.host, self.get_endpoint(), project_id)

    def create(self, name, description=None):
        params = {
            'name': name,
            'description': description
        }
        resp = requests.post(
            self.general_url, headers=self.get_auth_header(), data=params)

        return Project.from_dict(resp.json())

    def update(self, project_id, name, description=None):
        params = {
            'name': name,
            'description': description
        }
        resp = requests.patch(
            self.specific_url(project_id),
            headers=self.get_auth_header(),
            data=params
        )
        data = resp.json()

        if resp.status_code >= 400 and resp.status_code < 500:
            errors = " ".join(data.values())
            error_msg = "{0} - {1}".format(resp.status_code, errors)
            raise requests.HTTPError(error_msg, response=resp)

        return Project.from_dict(data)

    def delete(self, project_id):
        resp = requests.delete(
            self.specific_url(project_id), headers=self.get_auth_header())

        if resp.status_code >= 400 and resp.status_code < 500:
            data = resp.json()
            errors = " ".join(data.values())
            error_msg = "{0} - {1}".format(resp.status_code, errors)
            raise requests.HTTPError(error_msg, response=resp)
        elif resp.status_code == 204:
            return True

        raise Exception('Unexpected status code: {0}'.format(resp.status_code))

    def get(self, project_id):
        resp = requests.get(
            self.specific_url(project_id), headers=self.get_auth_header())
        data = resp.json()

        if resp.status_code >= 400 and resp.status_code < 500:
            errors = " ".join(data.values())
            error_msg = "{0} - {1}".format(resp.status_code, errors)
            raise requests.HTTPError(error_msg, response=resp)

        return Project.from_dict(data)

    def list(self):
        resp = requests.get(self.general_url, headers=self.get_auth_header())
        data = resp.json()

        if resp.status_code >= 400 and resp.status_code < 500:
            errors = " ".join(data.values())
            error_msg = "{0} - {1}".format(resp.status_code, errors)
            raise requests.HTTPError(error_msg, response=resp)

        return as_project_list(data)


class TasksService(Service):

    def get_endpoint(self, project_id):
        return '/api/projects/{0}/tasks/'.format(project_id)

    def list(self, project_id):
        url = '{0}{1}'.format(self.host, self.get_endpoint(project_id))
        resp = requests.get(url, headers=self.get_auth_header())
        data = resp.json()

        if resp.status_code >= 400 and resp.status_code < 500:
            errors = " ".join(data.values())
            error_msg = "{0} - {1}".format(resp.status_code, errors)
            raise requests.HTTPError(error_msg, response=resp)

        return as_task_list(data)
