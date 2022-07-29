from settings.environment.base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-foez$+0ren1#btn$8ay!mzoybqti$^n72-a!z4@4u%#ij6n88c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

HOST = str(os.environ.get("HOST", "localhost:9000"))
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# CORS Settings
# ------------------------------------------------------------------------------
X_FRAME_OPTIONS = 'SAMEORIGIN'
CSRF_TRUSTED_ORIGINS = [
    'http://localhost'
]
CSRF_COOKIE_SAMESITE = None
CSRF_COOKIE_HTTPONLY = False
CSRF_USE_SESSIONS = True

CORS_ALLOW_ALL_ORIGINS = bool(int(os.environ.get("CORS_ALLOW_ALL_ORIGINS", '1')))
CORS_ORIGIN_ALLOW_ALL = bool(int(os.environ.get("CORS_ORIGIN_ALLOW_ALL", '1')))
CORS_ORIGIN_WHITELIST = [
    'http://localhost',
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost',
]
