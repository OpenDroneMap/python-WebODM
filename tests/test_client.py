#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for Client class."""

import pytest
from webodm import Webodm, NonFieldErrors


@pytest.fixture
def client():
    return Webodm()


@pytest.fixture
def auth_client():
    return Webodm('user', 'password123')


# This method will be used by the mock to replace requests.get
def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    valid_url = 'http://localhost:8000/api/token-auth/'
    valid_data = {
        'username': 'user',
        'password': 'password123'
    }
    if args[0] == valid_url and kwargs.get('data') == valid_data:
        return MockResponse({'token': '123456'}, 200)

    return MockResponse({
        'non_field_errors': 'Unable to login with provided credentials.'
    }, 400)


def test_client_without_auth(client):
    assert client.token is None


def test_client_default_host(client):
    assert client.host == 'http://localhost:8000'


def test_client_auto_authenticate(mocker):
    mocker.patch('requests.post', side_effect=mocked_requests_post)
    client = Webodm('user', 'password123')
    assert client.token == '123456'


def test_client_missing_password():
    with pytest.raises(AttributeError) as e:
        Webodm(username='user')
    assert 'Username passed, but password is missing.' in str(e.value)


def test_client_missing_username():
    with pytest.raises(AttributeError) as e:
        Webodm(password='123456')
    assert 'Password passed, but username is missing.' in str(e.value)


def test_client_unable_to_login(mocker):
    mocker.patch('requests.post', side_effect=mocked_requests_post)
    with pytest.raises(NonFieldErrors) as e:
        Webodm('invalid', 'invalid')
    assert 'Unable to login with provided credentials.' in str(e.value)


def test_authenticate(mocker, client):
    mocker.patch('requests.post', side_effect=mocked_requests_post)
    client.authenticate('user', 'password123')
    assert client.token == '123456'
