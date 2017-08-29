#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""WebODM Client."""

from .services import AuthService, ProjectsService, TasksService

LOCAL_HOST = 'http://localhost:8000'


class Webodm(object):

    def __init__(self, username=None, password=None, host=LOCAL_HOST):
        if username is not None and password is None:
            raise AttributeError('Username passed, but password is missing.')
        elif username is None and password is not None:
            raise AttributeError('Password passed, but username is missing.')

        self.token = None
        self.host = host

        if username is not None and password is not None:
            self.token = AuthService(self.host).auth(username, password)

        self.projects = ProjectsService(self.host, self.token)
        self.tasks = TasksService(self.host, self.token)
