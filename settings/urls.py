"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('settings.urls'))
"""
import os

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from settings.environment.settings import \
    get_settings_module, environment, Environment
from settings.utils import schema_view

without_production_admin_patterns = []

match environment:
    case Environment.LOCAL:
        without_production_admin_patterns.append(path('admin/', admin.site.urls), )

settings = get_settings_module()

basepatterns = [
    # API URLS
    path('api/v1/', include(('apps.core.api.urls', 'core'), namespace='api-urls')),

    # CORE URLS
    path('', include(('apps.core.urls', 'core'), namespace='core-urls')),

    # SWAGGER URLS
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # REDOC URLS
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Editor urls
    path('editor/', include(('apps.editor.urls', 'editor'), namespace='editor-urls')),

    # mdeditor urls
    path('mdeditor/', include('mdeditor.urls')),

    # djrichtextfield urls
    path('djrichtextfield/', include('djrichtextfield.urls'))
]

basepatterns += static(settings.MEDIA_URL,
                       document_root=settings.MEDIA_ROOT)
basepatterns += static(settings.STATIC_URL,
                       document_root=settings.STATIC_ROOT)

urlpatterns = basepatterns + without_production_admin_patterns
