import os
from .base import *
from django.core.management.utils import get_random_secret_key


DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "*").split(",")

CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "*").split(",")

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

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "region_name": "nyc3",
            "endpoint_url": "https://portfolio-website-media.nyc3.cdn.digitaloceanspaces.com",
            "access_key": "portfolio-media",
            "secret_key": os.getenv("MEDIA_SECRET_KEY")

        }
    }
}

MEDIA_URL = "https://portfolio-website-media.nyc3.cdn.digitaloceanspaces.com"

try:
    from .local import *
except ImportError:
    pass
