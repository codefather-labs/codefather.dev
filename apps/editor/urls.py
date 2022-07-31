from django.urls import path

from apps.editor import views
from settings.environment.settings import get_settings_module

settings = get_settings_module()

urlpatterns = [
    path('', views.editor, name='editor-url'),
    path('<str:post_uuid>', views.editor, name='editor-post-url'),
    path('<str:post_uuid>/<str:lang_code>', views.editor, name='editor-lang-post-url'),
]

# ADMIN EDITOR
if settings.EDITOR_ROUTE_ENABLED:
    urlpatterns.append(
        path('post/markdown/<str:post_uuid>', views.post_markdown, name='post-markdown-url')
    )
