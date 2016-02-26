|Build Status|

cookiecutter-ansible-role
=========================

Cookiecutter template for Ansible role

Requirements
------------

Cookiecutter (>=1.3.0) (https://github.com/audreyr/cookiecutter)

It's easy to install it with pip.

How To
------

You can create new project of Ansible role as follows.

.. code:: bash

    $ cookiecutter gh:FGtatsuro/cookiecutter-ansible-role
    Cloning into 'cookiecutter-ansible-role'...
    remote: Counting objects: 99, done.
    remote: Compressing objects: 100% (66/66), done.
    remote: Total 99 (delta 32), reused 84 (delta 20), pack-reused 0
    Unpacking objects: 100% (99/99), done.
    Checking connectivity... done.
    
    role_project_name [Project name of Ansible role]: project_name
    role_name [Ansible role name]: role_name
    year [2016]:
    author [Your Github username]: FGtatsuro
    
    $ cd project_name
    $ ls
    Gemfile      LICENSE      Rakefile     defaults     handlers     roles        tasks        tests
    Gemfile.lock README.md    ansible.cfg  files        meta         spec         templates    vars

You can overwrite default value of the field prompt asks with `~/.cookiecutterrc`.
It's better to overwrite 'author' field with your Github username.

.. code:: bash

    $ cat ~/.cookiecutterrc
    default_context:
        author: "FGtatsuro"
    
    $ cookiecutter gh:FGtatsuro/cookiecutter-ansible-role
    ...
    author [FGtatsuro]: 

Attention
---------

Role dependency
^^^^^^^^^^^^^^^

Generated role project depends on the role `FGtatsuro.python-requirements`_ in default.
If your role don't need it, please fix `meta/main.yml` and `.travis.yml` in your role project.

Supported platforms
^^^^^^^^^^^^^^^^^^^

Generated role project supports Debian family(Debian/Ubuntu) and OSX in default.
Please check files under `tasks` directory. `Ansible document`_ is useful to understand them.

.. |Build Status| image:: https://travis-ci.org/FGtatsuro/cookiecutter-ansible-role.svg?branch=master
   :target: https://travis-ci.org/FGtatsuro/cookiecutter-ansible-role
.. _FGtatsuro.python-requirements: https://galaxy.ansible.com/FGtatsuro/python-requirements/
.. _Ansible document: http://docs.ansible.com/ansible/playbooks_conditionals.html
