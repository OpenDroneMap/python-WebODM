#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for AuthService."""

import pytest
from webodm import NonFieldErrors, LOCAL_HOST
from webodm.services import AuthService


@pytest.fixture
def authservice():
    return AuthService(LOCAL_HOST)


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


def mocked_auth(*args, **kwargs):
    valid_url = 'http://localhost:8000/api/token-auth/'
    valid_data = {
        'username': 'user',
        'password': 'password123'
    }

    if args[0] == valid_url:
        if kwargs.get('data') == valid_data:
            return MockResponse({'token': '123456'}, 200)

        return MockResponse({
            'non_field_errors': 'Unable to login with provided credentials.'
        }, 400)

    return MockResponse({'detail': 'Not Found.'}, 404)


def test_auth(mocker, authservice):
    mocker.patch('requests.post', side_effect=mocked_auth)
    token = authservice.auth('user', 'password123')
    assert token == '123456'


def test_authenticate_unable_to_login(mocker, authservice):
    mocker.patch('requests.post', side_effect=mocked_auth)
    with pytest.raises(NonFieldErrors) as e:
        authservice.auth('invalid', 'invalid')
    assert 'Unable to login with provided credentials.' in str(e.value)
