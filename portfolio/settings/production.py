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
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "region_name": "nyc3",
            "endpoint_url": "https://nyc3.digitaloceanspaces.com",
            "bucket_name": "portfolio-website-media",
            "access_key": os.getenv("MEDIA_ACCESS_KEY"),
            "secret_key": os.getenv("MEDIA_SECRET_KEY")
        }
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

AWS_ACCESS_KEY_ID = os.getenv("MEDIA_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.getenv("MEDIA_SECRET_KEY")
AWS_STORAGE_BUCKET_NAME = "portfolio-website-media"
AWS_S3_ENDPOINT_URL = "https://nyc3.digitaloceanspaces.com"
AWS_S3_REGION_NAME = "nyc3"
AWS_S3_ADDRESSING_STYLE = "virtual"
AWS_DEFAULT_ACL = None  # Important to avoid access denied

MEDIA_URL = "https://portfolio-website-media.nyc3.cdn.digitaloceanspaces.com/media/"

STATIC_URL = "/assets/"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}

MIDDLEWARE += ["django.middleware.common.BrokenLinkEmailsMiddleware"]

ADMINS = [("Chelsie", "chelsieminor@gmail.com")]

try:
    from .local import *
except ImportError:
    pass
