from .base import *
import dj_database_url
from decouple import config

DATABASES = {
    'default': {
        **dj_database_url.parse(config('DATABASE_URL')),
        'ENGINE': 'django.db.backends.postgresql',
    }
}