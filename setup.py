#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os

from setuptools import setup

# Package meta-data.
NAME = 'ainv'
DESCRIPTION = 'Ansible inventory creation'
URL = 'https://github.com/ducksify/chuv-inventory'
EMAIL = 'fegger@ducksify.com'
AUTHOR = 'François Egger'
VERSION = '0.1.0'

# What packages are required for this module to be executed?
REQUIRED = [
    'sqlalchemy', 'cx_oracle'
]

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Where the magic happens:
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    python_requires='>=3.6.0',
    # If your package is a single module, use this instead of 'packages':
    py_modules=['main'],

    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # $ setup.py publish support.
    entry_points={"console_scripts":
                      ["ainv=main:menuentry"]
                  },
)
