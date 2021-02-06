#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='{{ cookiecutter.project_name }}',
    version='0.0.0',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    author_email='',
    url='',  # replace with your own github repo url
    install_requires=['pytorch-lightning', 'hydra-core'],
    packages=find_packages(),
    license='{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %}' # noqa
)
