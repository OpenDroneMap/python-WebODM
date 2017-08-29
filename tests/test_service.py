#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for Service."""

import pytest

from webodm import LOCAL_HOST
from webodm.exceptions import ImproperlyConfigured
from webodm.services import Service


def test_get_auth_header_ok():
    service = Service(LOCAL_HOST, '123456')
    auth_header = service.get_auth_header()
    assert auth_header == {'Authorization': 'JWT {0}'.format('123456')}


def test_get_auth_header_exception():
    service = Service(LOCAL_HOST)
    with pytest.raises(ImproperlyConfigured) as e:
        service.get_auth_header()
    assert ("No token configured. Pass a token to the Service"
            " contructor or set it's value.") in str(e.value)
