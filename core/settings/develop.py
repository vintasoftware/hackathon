
from decouple import config

from .local import *

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': config('DATABASE_USER', default=''),
        'NAME': config('DATABASE_NAME', default=''),
        'PASSWORD': config('DATABASE_PASSWORD', default=''),
        'HOST': config('DATABASE_HOST', default=''),
        'ATOMIC_REQUESTS': True,
    }
}
