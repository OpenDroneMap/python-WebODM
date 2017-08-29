#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for TasksService."""

import pytest
from requests import HTTPError

from webodm import LOCAL_HOST
from webodm.models import Task
from webodm.services import TasksService


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


@pytest.fixture
def tasks():
    return TasksService(LOCAL_HOST, '123456')


@pytest.fixture
def task_data(name=None, description=None):
    data = {
        "id": 134,
        "project": 27,
        "processing_node": 10,
        "images_count": 48,
        "available_assets": [
            "all.zip",
            "orthophoto.tif",
            "orthophoto.png",
            "georeferenced_model.las",
            "georeferenced_model.ply",
            "georeferenced_model.csv",
            "textured_model.zip"
        ],
        "uuid": "4338d684-91b4-49a2-b907-8ba171894393",
        "name": "Task Name",
        "processing_time": 2197417,
        "auto_processing_node": False,
        "status": 40,
        "last_error": None,
        "options": [
            {
                "name": "use-opensfm-pointcloud",
                "value": True
            }
        ],
        "ground_control_points": None,
        "created_at": "2017-02-18T18:01:55.402551Z",
        "pending_action": None
    }
    return data


def task_list():
    data = [task_data()]
    return data


def mocked_request_list_ok(*args, **kwargs):
    return MockResponse(task_list(), 200)


def mocker_request_list_404(*args, **kwargs):
    return MockResponse({'detail': 'Not Found.'}, 404)


def test_list_ok(mocker, tasks, task_data):
    mocker.patch('requests.get', side_effect=mocked_request_list_ok)
    tasks = tasks.list(27)
    assert tasks == [Task.from_dict(task_data)]


def test_list_exception(mocker, tasks):
    mocker.patch('requests.get', side_effect=mocker_request_list_404)
    with pytest.raises(HTTPError) as e:
        tasks.list(1)
    assert '404 - Not Found.' == str(e.value)
