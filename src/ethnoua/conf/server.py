"""
ethnoua.conf.server
~~~~~~~~~~~~~~~~~~

These settings act as the default (base) settings for the Ethnoua-provided web-server

:copyright: (c) 2010-2013 by the Ethnoua Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from django.conf.global_settings import *  # NOQA

import hashlib
import os
import os.path
import socket
import sys
import urlparse

DEBUG = False
TEMPLATE_DEBUG = True

ADMINS = ()

INTERNAL_IPS = ('127.0.0.1',)

MANAGERS = ADMINS

APPEND_SLASH = True

PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), os.pardir))

sys.path.insert(0, os.path.normpath(os.path.join(PROJECT_ROOT, os.pardir)))

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sentry.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

if 'DATABASE_URL' in os.environ:
    url = urlparse.urlparse(os.environ['DATABASE_URL'])

    # Ensure default database exists.
    DATABASES['default'] = DATABASES.get('default', {})

    # Update with environment configuration.
    DATABASES['default'].update({
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
    })
    if url.scheme == 'postgres':
        DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'

    if url.scheme == 'mysql':
        DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'

EMAIL_SUBJECT_PREFIX = '[Ethnoua] '

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

USE_TZ = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = hashlib.md5(socket.gethostname() + ')*)&8a36)6%74e@-ne5(-!8a(vv#tkv)(eyg&@0=zd^pl!7=y@').hexdigest()

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'ethnoua.conf.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.csrf',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django_extensions',
    'gunicorn',

    'south',
    'ethnoua'
)

SOUTH_MIGRATION_MODULES = {
    'ethnoua': 'ethnoua.migrations',
}

STATIC_ROOT = os.path.realpath(os.path.join(PROJECT_ROOT, 'static'))
STATIC_URL = '/_static/'

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "static_compiler.finders.StaticCompilerFinder",
)

LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
)
