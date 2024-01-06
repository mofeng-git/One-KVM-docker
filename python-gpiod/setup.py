#!/usr/bin/env python3
#
# Setup script for standalone libgpiod Python bindings.
#
# SPDX-License-Identifier: LGPL-2.1-or-later
# Copyright (C) 2020 Allen Wild <allenwild93@gmail.com>

import sys
if sys.version_info < (3,):
    sys.exit('Error: this module requires Python 3')

from setuptools import Extension, setup

gpiod_version = '1.5.1'
gpiod_headers = ['gpiod/gpiod.h', 'gpiod/linux/gpio.h']
gpiod_extension = Extension(
    name='gpiod',
    sources=[
        # gpiod Python module
        'gpiod/gpiodmodule.c',
        # libgpiod C API
        'gpiod/core.c',
        'gpiod/helpers.c',
        'gpiod/iter.c',
        'gpiod/misc.c',
        #'gpiod/ctxless.c', # not needed by python bindings
    ],
    include_dirs=['gpiod'],
    define_macros=[('_GNU_SOURCE', None), ('GPIOD_VERSION_STR', '"%s"'%gpiod_version)],
    depends=gpiod_headers,
)

with open('README.md', 'r') as fp:
    readme_content = fp.read()

setup(
    name='gpiod',
    ext_modules=[gpiod_extension],

    version=gpiod_version,
    description='Standalone libgpiod Python bindings',
    long_description=readme_content,
    long_description_content_type='text/markdown',
    maintainer='Allen Wild',
    maintainer_email='allenwild93@gmail.com',
    url='https://github.com/aswild/python-gpiod',
    python_requires='>=3',
    classifiers=[
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: POSIX :: Linux',
    ]
)
