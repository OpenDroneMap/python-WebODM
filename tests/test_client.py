#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for Client class."""

import pytest
from webodm import Webodm


@pytest.fixture
def client():
    return Webodm()


@pytest.fixture
def auth_client():
    return Webodm('user', 'password123')


def mocked_token(*args, **kwargs):
    return '123456'


def test_default_host(client):
    assert client.host == 'http://localhost:8000'


def test_init_without_params(client):
    assert client.token is None


def test_init_ok(mocker):
    mocker.patch('webodm.services.AuthService.auth', side_effect=mocked_token)
    client = Webodm('user', 'password123')
    assert client.token == '123456'


def test_init_missing_password():
    with pytest.raises(AttributeError) as e:
        Webodm(username='user')
    assert 'Username passed, but password is missing.' in str(e.value)


def test_init_missing_username():
    with pytest.raises(AttributeError) as e:
        Webodm(password='123456')
    assert 'Password passed, but username is missing.' in str(e.value)
