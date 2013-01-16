#!/usr/bin/env python

import os
from setuptools import setup, find_packages

def requirements(filename):
  with open(os.path.abspath(os.path.join(os.path.dirname(__file__), filename))) as f:
    f.readlines()

setup(name='phpbb-python',
      version='0.0.1',
      description='phpBB authentication in Python',
      author='Santtu Pajukanta',
      author_email='santtu@pajukanta.fi',
      url='https://github.com/japsu/phpbb-python',
      packages=find_packages()
      )