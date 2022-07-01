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

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from settings.environment.settings import get_settings_module
from settings.utils import schema_view

settings = get_settings_module()

urlpatterns = [
    path('admin/', admin.site.urls),

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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
