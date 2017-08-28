#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for Models."""

import pytest
from webodm.models import Project


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


def test_from_dict(project_data):
    project = Project.from_dict(project_data)

    assert (
        project.id == 2 and
        project.tasks == [1, 2] and
        project.created_at == '2016-12-07T02:09:28.515319Z' and
        project.name == 'Test' and
        project.description == 'Test test' and
        project.permissions == ['delete', 'change', 'add', 'view']
    )
