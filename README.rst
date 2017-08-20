=============
python-WebODM
=============


.. image:: https://img.shields.io/pypi/v/python_webodm.svg
        :target: https://pypi.python.org/pypi/python_webodm

.. image:: https://img.shields.io/travis/rmallermartins/python-WebODM.svg
        :target: https://travis-ci.org/rmallermartins/python-WebODM

.. image:: https://readthedocs.org/projects/python-webodm/badge/
        :target: https://python-webodm.readthedocs.io/en/latest/
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/rmallermartins/python-WebODM/shield.svg
     :target: https://pyup.io/repos/github/rmallermartins/python-WebODM/
     :alt: Updates


Python client for WebODM API


* Free software: MIT license
* Documentation: https://python-webodm.readthedocs.io.

Development Guideline
---------------------

* Using https://github.com/charlesthk/python-mailchimp ans https://github.com/gophish/api-client-python as basis API Client, they seem to have a nice structure but still simpler then others.


API Structure
=============

WebODM

* Projects

  - Tasks
* Processing Nodes

API Objects and Calls
=====================

Projects:

* create(params)
* update(id, params)
* delete(id)
* list(?params)

Tasks:

* create(project_id, params)
* update(project_id, task_id, params)
* delete(project_id, task_id)
* list(project_id, ?params)
* download(project_id, task_id, asset)
* assets(project_id, task_id, path)
* output(project_id, task_id, ?line)
* cancel(project_id, task_id)
* remove(project_id, task_id)
* restart(project_id, task_id)
* tiles(project_id, task_id, ?zxy)

Processing Nodes:

* add(params)
* update(params)
* delete()
* list(params)
* options()

*?: Optional parameter*

Features
--------

* Create API Client (duh!)

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
