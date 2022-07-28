from typing import Union
from uuid import UUID

from django.http import Http404
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from rest_framework.request import Request

from apps.core.models import Post, Tag
from apps.core.utils import create_context
from settings.logger import system_message


def main(request: Request):
    return render(
        request,
        'site/base.html',
        create_context('main')
    )


def resume(request: Request):
    return render(
        request,
        'site/resume.html',
        create_context('resume')
    )


def projects(request: Request):
    return render(
        request,
        'site/projects.html',
        create_context('projects')
    )


def blog(request: Request):
    return render(
        request,
        'site/blog.html',
        create_context('blog')
    )


def contacts(request: Request):
    return render(
        request,
        'site/contacts.html',
        create_context('contacts')
    )


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
        "tag": {
            "title": tag.title,
        }, **create_context('blog')
    })


@cache_page(60 * 30)
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
        "post": post, **create_context('blog')
    })
