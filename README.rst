==============================
python-WebODM (In Development)
==============================


.. image:: https://img.shields.io/pypi/v/python_webodm.svg
        :target: https://pypi.python.org/pypi/python_webodm

.. image:: https://img.shields.io/travis/OpenDroneMap/python-WebODM.svg
        :target: https://travis-ci.org/OpenDroneMap/python-WebODM

.. image:: https://readthedocs.org/projects/python-webodm/badge/
        :target: https://python-webodm.readthedocs.io/en/latest/
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/OpenDroneMap/python-WebODM/shield.svg
     :target: https://pyup.io/repos/github/OpenDroneMap/python-WebODM/
     :alt: Updates


Python client for WebODM API


* Free software: MIT license
* Documentation: https://python-webodm.readthedocs.io.

Development Guideline
---------------------

* Using https://github.com/charlesthk/python-mailchimp ans https://github.com/gophish/api-client-python as basis API Client, they seem to have a nice structure but still simpler then others.


Roadmap
-------

* [X] Client Class (Webodm)
* ProjectsService

  - [X] Project Class
  - [X] Create
  - [X] Update
  - [X] Delete
  - [X] Get
  - [X] List
  - [ ] Get and List filters
* TasksService

  - [ ] Task Class
  - [ ] Create
  - [ ] Update
  - [ ] Delete
  - [ ] Get
  - [ ] List
  - [ ] Get and List filters
  - ...
* Node Service

  - ...
* [X] Extract AuthService from Webodm

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
