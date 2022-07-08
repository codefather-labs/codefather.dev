from django.urls import path

from apps.editor import views

urlpatterns = [
    path('', views.editor, name='editor-url'),
    path('<str:post_uuid>', views.editor, name='editor-post-url'),
    path('<str:post_uuid>/<str:lang_code>', views.editor, name='editor-lang-post-url'),
]
