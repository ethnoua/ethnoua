from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys


dev_requires = [
    'flake8>=2.0,<2.1',
]


tests_require = [
    'exam>=0.5.1',
    'eventlet',
    'httpretty',
    'pytest',
    'pytest-cov>=1.4',
    'pytest-django',
    'pytest-timeout',
    'python-coveralls',
    'nydus',
    'mock>=0.8.0',
    'redis',
    'unittest2',
]


setup(
    name='ethnoua',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'Django>=1.5.4,<1.6',
        'logan',
        'south',
        'psycopg2',
        'django-extensions',
        'PIL',
        'django-storages',
        'ipython',
        'ipdb',
        'gunicorn',
        'werkzeug',
        'boto'
        ],
    extras_require={
        'tests': tests_require,
        'dev': dev_requires
    },
    entry_points={
        'console_scripts': [
            'ethnoua = ethnoua.utils.runner:main',
        ],
    },
)
