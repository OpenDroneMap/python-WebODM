#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Models classes for returning results."""


class Project(object):

    def __init__(self, id, tasks, created_at, name, description, permissions):
        self.id = id
        self.tasks = tasks
        self.created_at = created_at
        self.name = name
        self.description = description
        self.permissions = permissions

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @staticmethod
    def from_dict(dct):
        return Project(
            id=dct['id'],
            tasks=dct['tasks'],
            created_at=dct['created_at'],
            name=dct['name'],
            description=dct['description'],
            permissions=dct['permissions']
        )


def as_project_list(dct):
    return [Project.from_dict(x) for x in dct.get('results', [])]


class Task(object):

    def __init__(
            self, id, project, processing_node, images_count, available_assets,
            uuid, name, processing_time, auto_processing_node, status,
            last_error, options, ground_control_points, created_at,
            pending_action):
        self.id = id
        self.project = project
        self.processing_node = processing_node
        self.images_count = images_count
        self.available_assets = available_assets
        self.uuid = uuid
        self.name = name
        self.processing_time = processing_time
        self.auto_processing_node = auto_processing_node
        self.status = status
        self.last_error = last_error
        self.options = options
        self.ground_control_points = ground_control_points
        self.created_at = created_at
        self.pending_action = pending_action

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @staticmethod
    def from_dict(dct):
        return Task(
            id=dct['id'],
            project=dct['project'],
            processing_node=dct['processing_node'],
            images_count=dct['images_count'],
            available_assets=dct['available_assets'],
            uuid=dct['uuid'],
            name=dct['name'],
            processing_time=dct['processing_time'],
            auto_processing_node=dct['auto_processing_node'],
            status=dct['status'],
            last_error=dct['last_error'],
            options=dct['options'],
            ground_control_points=dct['ground_control_points'],
            created_at=dct['created_at'],
            pending_action=dct['pending_action'],
        )


def as_task_list(data):
    return [Task.from_dict(x) for x in data]
