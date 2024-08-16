#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(
        include=['src', 'src.*']
    ),
    test_suite='tests',
    version="0.1.0",
)
