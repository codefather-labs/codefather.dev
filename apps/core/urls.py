from django.urls import path, include

from apps.core import views as core_views
from apps.editor.urls import urlpatterns as editor_patterns

core_patterns = [
    path('', core_views.main, name='main_url'),
    path('resume', core_views.resume, name='resume_url'),
    path('projects', core_views.projects, name='projects_url'),
    path('blog/', core_views.blog, name='blog_url'),
    path('blog/tag/<str:reference>', core_views.tag, name='tag_url'),
    path('blog/post/<str:reference>', core_views.post, name='post_url'),
    path('contacts', core_views.contacts, name='contacts_url'),
]

urlpatterns = []
urlpatterns += core_patterns

