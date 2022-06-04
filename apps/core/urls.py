from django.urls import path

from apps.core import views as core_views

core_patterns = [
    path('', core_views.main, name='main_url'),
    path('test', core_views.test, name='test_url')
]

urlpatterns = []
urlpatterns += core_patterns
