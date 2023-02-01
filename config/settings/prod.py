from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': env.db_url(
        'DEV_DATABASE_URL',
        default='mysql://root:1q2w3e4r@172.23.0.5:3306/lime_hr_dev'
    ),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'cola': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    },
}