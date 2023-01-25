from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': env.db_url(
        'DEV_DATABASE_URL',
        default='mysql://root:1q2w3e4r!@172.7.0.2:3320/lime_hr_dev'
    ),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'cola': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    },
}