from django.urls import path

from apps.editor import views

urlpatterns = [
    path('', views.editor, name='editor-url'),
    path('<str:edited_post_view_uuid>', views.editor, name='editor-post-url'),
]
