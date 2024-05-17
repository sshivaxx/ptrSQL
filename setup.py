#!/usr/bin/env python

import sys
from os.path import join, dirname
from setuptools import setup, find_packages

sys.path.append(join(dirname(__file__), 'src'))

from ptrSQL import __version__ as version

setup(
    name='ptrSQL',
    version=version,
    packages=find_packages('src', include=['ptrSQL', 'ptrSQL.*']),
    package_dir={'ptrSQL': 'src/ptrSQL'},
    entry_points={
        'console_scripts':
            ['ptrSQL = ptrSQL.repl:launch']
    }
)
