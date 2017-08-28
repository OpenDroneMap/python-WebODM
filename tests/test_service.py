import pytest

from webodm import LOCAL_HOST
from webodm.exceptions import ImproperlyConfigured
from webodm.services import Service


class EndpointService(Service):
    endpoint = '/api/'


class NoEndpointService(Service):
    pass


def test_get_endpoint_ok():
    service = EndpointService(LOCAL_HOST, '123456')
    endpoint = service.get_endpoint()
    assert endpoint == '/api/'


def test_get_endpoint_exception():
    service = NoEndpointService(LOCAL_HOST, '123456')
    with pytest.raises(ImproperlyConfigured) as e:
        service.get_endpoint()
    assert 'No endpoint configured. Provide an endpoint.' in str(e.value)


def test_get_auth_header_ok():
    service = EndpointService(LOCAL_HOST, '123456')
    auth_header = service.get_auth_header()
    assert auth_header == {'Authorization': 'JWT {0}'.format('123456')}


def test_get_auth_header_exception():
    service = EndpointService(LOCAL_HOST)
    with pytest.raises(ImproperlyConfigured) as e:
        service.get_auth_header()
    assert ("No token configured. Pass a token to the Service"
            " contructor or set it's value.") in str(e.value)
