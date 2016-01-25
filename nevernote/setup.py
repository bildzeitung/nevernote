#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='nevernote',
    description='NCurses client for Evernote',
    author='bildzeitung',
    author_email='bildzeitung@gmail.com',
    url='http://casa.blan.ca',
    packages=find_packages(exclude=["tests"]),
    test_suite='nose.collector',
    setup_requires=['vcversioner'],
    install_requires=[
    ],
    tests_require=[
    ],
    vcversioner={}
)
