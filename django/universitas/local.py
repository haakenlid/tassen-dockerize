""" Settings for local development """

from .dev import *  # noqa
from .dev import (
    DEBUG, INSTALLED_APPS, MIDDLEWARE_CLASSES, DATABASES,
)

DEFAULT_FROM_EMAIL = 'localemail@localhost'
# DATABASES['prodsys'].update({'HOST': 'localhost', })
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

RUNSERVERPLUS_SERVER_ADDRESS_PORT = '0.0.0.0:8000'
ALLOWED_HOSTS = '*'
# TOOLBAR CONFIGURATION
INSTALLED_APPS += ['debug_toolbar', ]
MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# Use File system in local development instead of Amanon S3
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
THUMBNAIL_STORAGE = DEFAULT_FILE_STORAGE
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

MEDIA_ROOT = '/media/'
STATIC_ROOT = '/static/'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}

DATABASES['prodsys'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'prodsys',
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': './',  # must end with slash
        'STATS_FILE': '/build/webpack-stats.json',
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}
