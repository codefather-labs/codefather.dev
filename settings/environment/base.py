from settings.logger import system_message

"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.contrib.staticfiles.utils import check_settings as check_django_settings
from corsheaders.checks import check_settings as check_cors_settings

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SITE_ID = 1

# A dictionary of urlconf module paths, keyed by their subdomain.
SUBDOMAIN_URLCONFS = {
    None: 'settings.urls',  # no subdomain, e.g. ``example.com``
    'www': 'settings.urls',
    # 'market': 'apps.market.urls',
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# Application definition
PRE_ADMIN_APPS = []
ROOT_APPS = [
    'apps.core',
    'apps.editor',
    # 'apps.market',
]
INSTALLED_APPS = [
    'corsheaders',
    'rest_framework',
    'drf_yasg',
    'mdeditor',
    'ckeditor',
    'djrichtextfield',
    'subdomains'
]

INSTALLED_APPS = [
    *PRE_ADMIN_APPS,
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    *INSTALLED_APPS,
    *ROOT_APPS
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'subdomains.middleware.SubdomainURLRoutingMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/
LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

languages = ['en', 'pl', 'ua', 'ja', 'de', 'fr', 'it', 'ja', 'cn', 'ru']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST_FRAMEWORK
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
}

# MDEditor Settings
# ------------------------------------------------------------------------------
MDEDITOR_CONFIGS = {
    'default': {
        'width': '100% ',  # Custom edit box width
        'height': 500,  # Custom edit box height
        'toolbar': ["undo", "redo", "|",
                    "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
                    "h1", "h2", "h3", "h5", "h6", "|",
                    "list-ul", "list-ol", "hr", "|",
                    "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime",
                    "emoji", "html-entities", "pagebreak", "goto-line", "|",
                    "help", "info",
                    "||", "preview", "watch", "fullscreen"],  # custom edit box toolbar
        'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],  # image upload format type
        'image_folder': 'editor',  # image save the folder name
        'theme': 'default',  # edit box theme, dark / default
        'preview_theme': 'default',  # Preview area theme, dark / default
        'editor_theme': 'default',  # edit area theme, pastel-on-dark / default
        'toolbar_autofixed': True,  # Whether the toolbar capitals
        'search_replace': True,  # Whether to open the search for replacement
        'emoji': True,  # whether to open the expression function
        'tex': True,  # whether to open the tex chart function
        'flow_chart': True,  # whether to open the flow chart function
        'sequence': True,  # Whether to open the sequence diagram function
        'watch': True,  # Live preview
        'lineWrapping': True,  # lineWrapping
        'lineNumbers': True,  # lineNumbers
        'language': 'en',  # zh / en / es
        "mode": "markdown",
        "markdown": True,
        "appendMarkdown": True,
    }
}

DJRICHTEXTFIELD_CONFIG = {
    'js': ['//cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js'],
    'init_template': 'djrichtextfield/init/tinymce.js',
    'settings': {
        'menubar': True,
        'plugins': 'link image',
        'toolbar': 'bold italic | link image | removeformat',
        'width': 1100,
        'height': 600
    }
}

# CORS Settings
# ------------------------------------------------------------------------------
X_FRAME_OPTIONS = 'SAMEORIGIN'
CSRF_COOKIE_SAMESITE = None
CSRF_COOKIE_HTTPONLY = False
CSRF_USE_SESSIONS = True
CORS_ALLOW_ALL_ORIGINS = bool(int(os.environ.get("CORS_ALLOW_ALL_ORIGINS", '1')))
CORS_ORIGIN_ALLOW_ALL = bool(int(os.environ.get("CORS_ORIGIN_ALLOW_ALL", '1')))
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'cache-control',
    'x-signature',
    'x-frame-options',
    "Access-Control-Allow-Origin",
    "Access-Control-Allow-Methods",
    "Access-Control-Max-Age",
    "Access-Control-Allow-Headers",
]

DEFAULT_FRONTEND_THEME = os.environ.get('DEFAULT_FRONTEND_THEME', 'black')
