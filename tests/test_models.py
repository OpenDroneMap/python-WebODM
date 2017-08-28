#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for Models."""

import pytest
from webodm.models import Project, Task


@pytest.fixture
def project_data(name=None, description=None):
    data = {
        "id": 2,
        "tasks": [1, 2],
        "created_at": "2016-12-07T02:09:28.515319Z",
        "name": "Test",
        "description": "Test test",
        "permissions": ["delete", "change", "add", "view"]
    }
    return data


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


def test_project():
    project = Project(
        id=2,
        tasks=[1, 2],
        created_at='2016-12-07T02:09:28.515319Z',
        name='Test',
        description='Test test',
        permissions=['delete', 'change', 'add', 'view']
    )

    assert (
        project.id == 2 and
        project.tasks == [1, 2] and
        project.created_at == '2016-12-07T02:09:28.515319Z' and
        project.name == 'Test' and
        project.description == 'Test test' and
        project.permissions == ['delete', 'change', 'add', 'view']
    )


def test_project_from_dict(project_data):
    project = Project.from_dict(project_data)

    assert (
        project.id == 2 and
        project.tasks == [1, 2] and
        project.created_at == '2016-12-07T02:09:28.515319Z' and
        project.name == 'Test' and
        project.description == 'Test test' and
        project.permissions == ['delete', 'change', 'add', 'view']
    )


def test_task():
    available_assets = [
        "all.zip",
        "orthophoto.tif",
        "orthophoto.png",
        "georeferenced_model.las",
        "georeferenced_model.ply",
        "georeferenced_model.csv",
        "textured_model.zip"
    ]
    options = [
        {
            "name": "use-opensfm-pointcloud",
            "value": True
        }
    ]
    task = Task(
        id=134,
        project=27,
        processing_node=10,
        images_count=48,
        available_assets=available_assets,
        uuid="4338d684-91b4-49a2-b907-8ba171894393",
        name="Task Name",
        processing_time=2197417,
        auto_processing_node=False,
        status=40,
        last_error=None,
        options=options,
        ground_control_points=None,
        created_at="2017-02-18T18:01:55.402551Z",
        pending_action=None,
    )

    assert (
        task.id == 134 and
        task.project == 27 and
        task.processing_node == 10 and
        task.images_count == 48 and
        task.available_assets == available_assets and
        task.uuid == "4338d684-91b4-49a2-b907-8ba171894393" and
        task.name == "Task Name" and
        task.processing_time == 2197417 and
        task.auto_processing_node is False and
        task.status == 40 and
        task.last_error is None and
        task.options == options and
        task.ground_control_points is None and
        task.created_at == "2017-02-18T18:01:55.402551Z" and
        task.pending_action is None
    )


def test_project_from_dict(task_data):
    available_assets = [
        "all.zip",
        "orthophoto.tif",
        "orthophoto.png",
        "georeferenced_model.las",
        "georeferenced_model.ply",
        "georeferenced_model.csv",
        "textured_model.zip"
    ]
    options = [
        {
            "name": "use-opensfm-pointcloud",
            "value": True
        }
    ]

    task = Task.from_dict(task_data)

    assert (
        task.id == 134 and
        task.project == 27 and
        task.processing_node == 10 and
        task.images_count == 48 and
        task.available_assets == available_assets and
        task.uuid == "4338d684-91b4-49a2-b907-8ba171894393" and
        task.name == "Task Name" and
        task.processing_time == 2197417 and
        task.auto_processing_node is False and
        task.status == 40 and
        task.last_error is None and
        task.options == options and
        task.ground_control_points is None and
        task.created_at == "2017-02-18T18:01:55.402551Z" and
        task.pending_action is None
    )
