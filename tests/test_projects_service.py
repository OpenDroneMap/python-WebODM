#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for ProjectsService class."""

import pytest
from requests import HTTPError
from webodm import ProjectsService


@pytest.fixture
def projects():
    return ProjectsService()


@pytest.fixture
def project_data(name=None, description=None):
    data = {
        "id": 1,
        "tasks": [7, 6, 5],
        "created_at": "2016-12-07T02:09:28.515319Z",
        "name": "Test" if name is None else name,
        "description": "" if description is None else description,
        "permissions": ["delete", "change", "add", "view"]
    }
    return data


def mocked_request_delete(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'http://localhost:8000/api/projects/1/':
        return MockResponse({}, 204)
    elif args[0] == 'http://localhost:8000/api/projects/10/':
        return MockResponse({}, 300)

    return MockResponse({'detail': 'Not Found.'}, 404)

# This method will be used by the mock to replace requests.get
def mocked_requests(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'http://localhost:8000/api/projects/1/':
        if kwargs.get('data', None) is not None:
            data = project_data(
                kwargs.get('data').get('name'),
                kwargs.get('data').get('description')
            )
            return MockResponse(data, 200)
        return MockResponse(project_data(), 200)
    elif args[0] == 'http://localhost:8000/api/projects/':
        data = project_data(
            kwargs.get('data').get('name'),
            kwargs.get('data').get('description')
        )
        return MockResponse(data, 200)

    return MockResponse({'detail': 'Not Found.'}, 404)


def test_projects_service_init(projects):
    assert projects.endpoint == '/api/projects/'


def test_create_ok(mocker, projects, project_data):
    mocker.patch('requests.post', side_effect=mocked_requests)
    data = projects.create('Project One', 'Test description')
    project_data['name'] = 'Project One'
    project_data['description'] = 'Test description'
    assert data == project_data


def test_update_ok(mocker, projects, project_data):
    mocker.patch('requests.patch', side_effect=mocked_requests)
    data = projects.update(1, 'Project Two', 'Test description edited')
    project_data['name'] = 'Project Two'
    project_data['description'] = 'Test description edited'
    assert data == project_data


def test_update_not_found(mocker, projects, project_data):
    with pytest.raises(HTTPError) as e:
        mocker.patch('requests.patch', side_effect=mocked_requests)
        projects.update(2, 'Project Two', 'Test description edited')
    assert '404 - Not Found.' == str(e.value)


def test_delete(mocker, projects):
    mocker.patch('requests.delete', side_effect=mocked_request_delete)
    deleted = projects.delete(1)
    assert deleted


def test_delete_not_found(mocker, projects):
    with pytest.raises(HTTPError) as e:
        mocker.patch('requests.delete', side_effect=mocked_request_delete)
        projects.delete(2)
    assert '404 - Not Found.' == str(e.value)


def test_delete_unexpected_status_code(mocker, projects):
    with pytest.raises(Exception) as e:
        mocker.patch('requests.delete', side_effect=mocked_request_delete)
        projects.delete(10)
    assert 'Unexpected status code: 300' == str(e.value)


def test_get(mocker, projects, project_data):
    mocker.patch('requests.get', side_effect=mocked_requests)
    data = projects.get(1)
    assert data == project_data


def test_get_not_found(mocker, projects, project_data):
    with pytest.raises(HTTPError) as e:
        mocker.patch('requests.get', side_effect=mocked_requests)
        projects.get(2)
    assert '404 - Not Found.' == str(e.value)
