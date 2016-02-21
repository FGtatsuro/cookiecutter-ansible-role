[![Build Status](https://travis-ci.org/{{ cookiecutter.author }}/{{ cookiecutter.role_project_name }}.svg?branch=master)](https://travis-ci.org/FGtatsuro/{{ cookiecutter.role_project_name }})

ansible-ansible
===============

Ansible role for {{ cookiecutter.role_name }}

Requirements
------------

None.

Role Variables
--------------

None.

Dependencies
------------

- <The dependencies for your role>

Example Playbook
----------------

    - hosts: all
      roles:
         - { role: FGtatsuro.{{ cookiecutter.role_name }} }

Test on local Docker host
-------------------------

This project run tests on Travis CI, but we can also run then on local Docker host.
Please check `install`, `before_script`, and `script` sections of `.travis.yml`. 
We can use same steps of them for local Docker host.

Local requirements are as follows.

- Ansible (> 2.0.0)
- Docker (> 1.10.1)


License
-------

MIT