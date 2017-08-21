#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `python_webodm` package."""

import pytest
from requests import Response
from webodm import Webodm, NonFieldErrors


def test_invalid_credentials():
    with pytest.raises(NonFieldErrors) as e:
        Webodm('user', 'password')
    assert 'Unable to login with provided credentials.' == str(e.value)


def test_client(mocker):
    mocker.patch.object(Webodm, 'get_token')
    Webodm.get_token.return_value = '123456'
    client = Webodm('user', 'password123')
    Webodm.get_token.assert_called_with('user', 'password123')
    assert client.host is not None
    assert client.token is not None
