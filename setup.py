from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys


setup(
    name='ethnoua',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'Django>=1.5.4,<1.6',
        'logan',
        'south'
        ],
    entry_points={
        'console_scripts': [
            'ethnoua = ethnoua.utils.runner:main',
        ],
    },
)
