#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

# Use setuptools if we can
try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)
monoku_dir = 'kopy'

for dirpath, dirnames, filenames in os.walk(monoku_dir):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(dirpath.split(os.sep)))
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

#print data_files

setup(
    name='kopy',
    version='0.0.1',
    description='Django app for copies in a website',
    long_description='',
    author='monoku',
    author_email='dev@monoku.com',
    url='http://www.monoku.com',
    download_url='http://www.monoku.com/django',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Natural Language :: Spanish",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development"
    ],
    packages=packages,
    data_files=data_files,
    install_requires=[
        'django',
    ],
    zip_safe = True,
)
