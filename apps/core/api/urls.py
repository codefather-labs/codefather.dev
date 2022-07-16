from django.urls import path

from apps.core.api import views as api_views

urlpatterns = [
    path('post/<str:reference>', api_views.post, name='post-create-update-delete-endpoint'),
    path('post/get/<str:reference>', api_views.post_get, name='post-get-endpoint'),
]
