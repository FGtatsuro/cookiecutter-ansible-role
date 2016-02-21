#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# Use symlink to handle the difference between project name and role name.
os.symlink('../../{{ cookiecutter.role_project_name }}', 'roles/{{ cookiecutter.role_name }}')
