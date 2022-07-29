import ast
import os

from settings.environment.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get("DEBUG")))

SECURE_SSL_REDIRECT = bool(int(os.environ.get("SECURE_SSL_REDIRECT", "0")))

HOST = str(os.environ.get("HOST"))
ALLOWED_HOSTS = list(ast.literal_eval(os.environ.get("ALLOWED_HOSTS")))
ADMIN_ROUTER_ENABLED = bool(int(os.environ.get("ADMIN_ROUTER_ENABLED", "0")))
ADMIN_ROUTE = os.environ.get("ADMIN_ROUTE")
WHITENOISE_PACKAGE_REQUIRE = bool(int(os.environ.get("WHITENOISE_PACKAGE_REQUIRE", "0")))

# Middleware Settings
# ------------------------------------------------------------------------------
if WHITENOISE_PACKAGE_REQUIRE:
    MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')

# Database Settings
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASS"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT"),
        'ATOMIC_REQUESTS': True
    },
}

# Static Settings
# ------------------------------------------------------------------------------
if WHITENOISE_PACKAGE_REQUIRE:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

    # with cache
    # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# CORS Settings
# ------------------------------------------------------------------------------
CSRF_TRUSTED_ORIGINS = list(ast.literal_eval(os.environ.get('CSRF_TRUSTED_ORIGINS')))
CORS_ORIGIN_WHITELIST = list(ast.literal_eval(os.environ.get('CSRF_TRUSTED_ORIGINS')))
CORS_ALLOWED_ORIGINS = list(ast.literal_eval(os.environ.get('CSRF_TRUSTED_ORIGINS')))

# Checking Settings
# ------------------------------------------------------------------------------
django_settings_error = check_django_settings()
system_message(django_settings_error) if django_settings_error else None

cors_settings_error = check_cors_settings(CORS_ALLOW_HEADERS)
system_message(cors_settings_error) if cors_settings_error else None
