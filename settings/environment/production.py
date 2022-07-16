import ast

from settings.environment.local import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
HOST = str(os.environ.get("HOST"))

ALLOWED_HOSTS = list(ast.literal_eval(os.environ.get("ALLOWED_HOSTS")))

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

# CORS Settings
# ------------------------------------------------------------------------------
X_FRAME_OPTIONS = 'SAMEORIGIN'
CSRF_TRUSTED_ORIGINS = list(ast.literal_eval(os.environ.get('CSRF_TRUSTED_ORIGINS')))
CSRF_COOKIE_SAMESITE = None
CSRF_COOKIE_HTTPONLY = True
CSRF_USE_SESSIONS = True

CORS_ALLOW_ALL_ORIGINS = bool(int(os.environ.get("CORS_ALLOW_ALL_ORIGINS", '1')))
CORS_ORIGIN_ALLOW_ALL = bool(int(os.environ.get("CORS_ORIGIN_ALLOW_ALL", '1')))
CORS_ORIGIN_WHITELIST = list(ast.literal_eval(os.environ.get('CSRF_TRUSTED_ORIGINS')))

CORS_ALLOWED_ORIGINS = list(ast.literal_eval(os.environ.get('CSRF_TRUSTED_ORIGINS')))

django_settings_error = check_django_settings()
system_message(django_settings_error) if django_settings_error else None

cors_settings_error = check_cors_settings(CORS_ALLOW_HEADERS)
system_message(cors_settings_error) if cors_settings_error else None
