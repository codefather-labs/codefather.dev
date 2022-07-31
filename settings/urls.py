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
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include, URLPattern
from django.views.decorators.cache import cache_page

from apps.core import sitemaps
from settings.environment.settings import get_settings_module
from settings.utils import schema_view, custom_static_serve

settings = get_settings_module()

sitemaps = {
    "static": sitemaps.StaticSitemap,
    "posts": sitemaps.PostSitemap,
    "categories": sitemaps.CategorySitemap,
    "tags": sitemaps.TagSitemap
}

urlpatterns = [
    # sitemap.xml
    path('sitemap.xml', cache_page(86400)(sitemap), {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),

    # API URLS
    path('api/v1/', include(('apps.core.api.urls', 'core'), namespace='api-urls')),

    # CORE URLS
    path('', include(('apps.core.urls', 'core'), namespace='core-urls')),

    # MARKET URLS
    # path('market/', include(('apps.market.urls', 'market'), namespace='market-urls')),

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

if settings.ADMIN_ROUTER_ENABLED:
    urlpatterns.append(path(settings.ADMIN_ROUTE, admin.site.urls))

urlpatterns += custom_static_serve(settings.MEDIA_URL,
                                   document_root=settings.MEDIA_ROOT)
urlpatterns += custom_static_serve(settings.STATIC_URL,
                                   document_root=settings.STATIC_ROOT)
