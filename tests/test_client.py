#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `python_webodm` package."""

import pytest
from requests import Response
from webodm import Webodm, NonFieldErrors


# This method will be used by the mock to replace requests.get
def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'http://localhost:8000/api/token-auth/':
        return MockResponse({"token": "123456"}, 200)

    return MockResponse(None, 404)


def test_authenticate(mocker):
    mocker.patch('requests.post', side_effect=mocked_requests_post)
    client = Webodm()
    assert client.token is None
    client.authenticate('user', 'password123')
    assert client.token is not None


def test_client_auto_authenticate(mocker):
    mocker.patch('requests.post', side_effect=mocked_requests_post)
    client = Webodm('user', 'password123')
    assert client.host is not None
    assert client.token is not None


def test_client(mocker):
    client = Webodm()
    assert client.host is not None
    assert client.token is None
