
from .base import *


DEBUG = True

SECRET_KEY = 'd(nsti34x)&hy!u9=yhaitpho001g=w4iu*3ff2o^bs=a5&e*#'

STATIC_ROOT = base_dir_join('staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = base_dir_join('media')
MEDIA_URL = '/media/'

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATICFILES_DIRS = (
    base_dir_join('static'),
)

# CELERY
BROKER_BACKEND = 'memory'
CELERY_ALWAYS_EAGER = True

# EMAIL
INSTALLED_APPS += ('naomi',)
EMAIL_BACKEND = "naomi.mail.backends.naomi.NaomiBackend"
EMAIL_FILE_PATH = base_dir_join('tmp_email')

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
        'ATOMIC_REQUESTS': True,
    }
}

# READABILITY
READABILITY_TOKEN = 'dfbec17c85fea39815aac9a75322b86eb8866a2b'