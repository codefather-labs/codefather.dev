from typing import Union
from uuid import UUID

from django.http import Http404
from django.shortcuts import render
from django.http.response import HttpResponseNotFound
from django.views.decorators.cache import cache_page
from rest_framework.request import Request

from apps.core.models import Post, Tag, Category
from apps.core.utils import create_context


@cache_page(60 * 15)
def main(request: Request):
    return render(
        request,
        'site/base.html',
        create_context('main')
    )


@cache_page(60 * 15)
def resume(request: Request):
    return render(
        request,
        'site/resume.html',
        create_context('resume')
    )


@cache_page(60 * 15)
def projects(request: Request):
    return render(
        request,
        'site/projects.html',
        create_context('projects')
    )


@cache_page(60 * 15)
def blog(request: Request):
    return render(
        request,
        'site/blog.html',
        create_context('blog')
    )


@cache_page(60 * 15)
def contacts(request: Request):
    return render(
        request,
        'site/contacts.html',
        create_context('contacts')
    )


@cache_page(60 * 15)
def tag(request: Request, reference: str):
    ref = {}
    try:
        ref.update({"uuid": UUID(reference)})
    except (AttributeError, ValueError):
        ref.update({"name": reference})

    try:
        tag = Tag.objects.get(**ref)
    except Post.DoesNotExist:
        return Http404("Tag was not found")

    return render(request, 'site/tag.html', {
        "tag": {
            "title": tag.title,
        }, **create_context('blog')
    })


@cache_page(60 * 15)
def category(request: Request, reference: str):
    ref = {}
    try:
        ref.update({"uuid": UUID(reference)})
    except (AttributeError, ValueError):
        ref.update({"name": reference})

    try:
        category = Category.objects.get(**ref)
    except Category.DoesNotExist:
        return Http404("Category was not found")

    return render(request, 'site/tag.html', {
        "tag": {
            "title": category.title,
        }, **create_context('blog')
    })


@cache_page(60 * 15)
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

    if not post.is_published:
        return HttpResponseNotFound()

    return render(request, 'site/post.html', {
        "post": post, **create_context('blog')
    })
