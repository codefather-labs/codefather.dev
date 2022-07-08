from typing import Union
from uuid import UUID

from django.http import Http404
from django.shortcuts import render
from rest_framework.request import Request

from apps.core.models import Post, Tag
from settings.logger import system_message


def main(request: Request):
    return render(request, 'site/base.html', {
        "context": {
            "page": "main"
        },
        "latest_posts": Post.objects.order_by('-created_at')[:5]
    })


def resume(request: Request):
    return render(request, 'site/resume.html', {
        "context": {
            "page": "resume"
        },
        "latest_posts": Post.objects.order_by('-created_at')[:5]
    })


def projects(request: Request):
    return render(request, 'site/projects.html', {
        "context": {
            "page": "projects"
        },
        "latest_posts": Post.objects.order_by('-created_at')[:5]
    })


def blog(request: Request):
    return render(request, 'site/blog.html', {
        "context": {
            "page": "blog"
        },
        "latest_posts": Post.objects.order_by('-created_at')[:5]
    })


def contacts(request: Request):
    return render(request, 'site/contacts.html', {
        "context": {
            "page": "contacts"
        },
        "latest_posts": Post.objects.order_by('-created_at')[:5]
    })


def tag(request: Request, reference: str):
    ref = {}
    try:
        ref.update({"uuid": UUID(reference)})
    except (AttributeError, ValueError):
        ref.update({"name": reference})

    try:
        tag = Tag.objects.get(**ref)
    except Post.DoesNotExist:
        return Http404("Post was not found")

    return render(request, 'site/tag.html', {
        "context": {
            "page": "blog"
        },
        "tag": {
            "title": tag.title,
        },
        "latest_posts": Post.objects.order_by('-created_at')[:5]
    })


def post(request: Request, reference: Union[str, str]):
    ref = {}
    try:
        ref.update({"uuid": UUID(reference)})
    except (AttributeError, ValueError):
        ref.update({"slug": reference})

    try:
        post = Post.objects.get(**ref)
    except Post.DoesNotExist:
        return Http404("Post was not found")

    return render(request, 'site/post.html', {
        "context": {
            "page": "blog"
        },
        "post": post,
        "latest_posts": Post.objects.order_by('-created_at')[:5]
    })
