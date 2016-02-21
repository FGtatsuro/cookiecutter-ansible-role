|Build Status|

cookiecutter-ansible-role
=========================

Cookiecutter template for Ansible role

How To
======

You can create new project of Ansible role as follows.

```bash
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
author [If you use your Github username, it's easy to integrate Travis CI]: FGtatsuro

$ cd project_name
$ ls
Gemfile      LICENSE      Rakefile     defaults     handlers     roles        tasks        tests
Gemfile.lock README.md    ansible.cfg  files        meta         spec         templates    vars
```

You can overwrite default value of the field prompt asks with `~/.cookiecutterrc`.
It's better to overwrite 'author' field.

```bash
$ cat ~/.cookiecutterrc
default_context:
    author: "FGtatsuro"

$ cookiecutter gh:FGtatsuro/cookiecutter-ansible-role
...
author [FGtatsuro]: 
```

.. |Build Status| image:: https://travis-ci.org/FGtatsuro/cookiecutter-ansible-role.svg?branch=master
   :target: https://travis-ci.org/FGtatsuro/cookiecutter-ansible-role
