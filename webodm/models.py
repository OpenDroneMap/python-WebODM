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
