from django.urls import path

from apps.market import views

urlpatterns = [
    path('', views.base, name='base-url')
]
