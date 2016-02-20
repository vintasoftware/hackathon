
from decouple import config

from .base import *

DEBUG = False

SECRET_KEY = config('SECRET_KEY', default='')

# TODO - Set the allowed hosts

# STORAGES
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATIC_ROOT = base_dir_join('staticfiles')
STATIC_URL = '/static/'

# CELERY
BROKER_URL = config('REDIS_URL', default='')
CELERY_RESULT_BACKEND = config('REDIS_URL', default='')
CELERY_SEND_TASK_ERROR_EMAILS = True

# EMAIL
SERVER_EMAIL = config('SERVER_EMAIL', default='')
EMAIL_HOST = config('EMAIL_HOST', default='')
EMAIL_PORT = config('EMAIL_PORT', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')


from dj_database_url import parse as db_url

DATABASES = {
    'default': config('DATABASE_URL', cast=db_url)
}
