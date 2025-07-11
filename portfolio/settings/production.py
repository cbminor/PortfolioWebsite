import os
from .base import *
from django.core.management.utils import get_random_secret_key


DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "*").split(",")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "defaultdb",
        "USER": "doadmin",
        "PASSWORD": os.getenv("DATABASE_USER_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST"),
        "PORT": 25060,
        "OPTIONS": {
            "sslmode": "require",
        }
    }
}

try:
    from .local import *
except ImportError:
    pass
