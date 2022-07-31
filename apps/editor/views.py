import uuid
from typing import Optional

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import render, redirect

from apps.core.models import Post
from apps.editor.models import EditedPostView
from apps.editor.forms import EditedPostViewForm, MarkdownPostForm
from apps.editor.utils import formatted_markdown


@login_required(login_url='admin:login')
def post_markdown(request: HttpRequest, post_uuid: str):
    try:
        post: Optional[Post] = Post.objects.get(uuid=post_uuid)
    except (ValidationError, Post.DoesNotExist):
        return HttpResponseNotFound()

    if request.method == "POST":
        form = EditedPostViewForm(request.POST)
        markdown = form.data.get('markdown')
        post.markdown = markdown
        post.save()

    return render(request, 'admin/markdown_editor.html', {
        "error": False,
        "status": "Success",
        "details": {
            "form": MarkdownPostForm(instance=post),
            "model": post,
            "markdown": formatted_markdown(post.markdown)
        }
    }, status=200)


@login_required(login_url='admin:login')
def editor(request: HttpRequest, post_uuid: str = None, lang_code: str = None):
    if request.method == "POST":
        data = {k: v[0] for k, v in dict(request.POST).items()}

        post = Post.objects.get(uuid=post_uuid)
        view: EditedPostView = EditedPostView.objects.get(source=post)
        data.update({"uuid": str(view.uuid)})

        form = EditedPostViewForm(data)

        if form.is_valid():
            data.pop('csrfmiddlewaretoken')
            if data.get('id_markdown-wmd-wrapper-html-code'):
                data.pop('id_markdown-wmd-wrapper-html-code')

            data['markdown'] = EditedPostViewForm.swap_delimiters(data['markdown'])

            instances: QuerySet[EditedPostView] = EditedPostView.objects.filter(
                uuid=data['uuid'],
                source=post
            )
            instances.update(**data)

            view = instances.last()

            return render(request, 'editor/editor.html', {
                "error": False,
                "status": "Success",
                "details": {
                    "form": EditedPostViewForm(instance=view),
                    "model": view
                }
            }, status=200)

        return render(request, 'editor/editor.html', {
            "error": True,
            "status": "Failed",
            "details": {
                "form": form,
                "model": None
            }
        }, status=200)

    post: Optional[Post] = None

    if post_uuid:
        try:
            post = Post.objects.get(uuid=post_uuid)
        except (ValidationError, Post.DoesNotExist):
            ...

    else:
        return redirect("editor-urls:editor-lang-post-url",
                        post_uuid=str(uuid.uuid4()),
                        lang_code=lang_code if lang_code else Post.DEFAULT_LANGUAGE)

    if not post:
        post, created = Post.objects.get_or_create(
            uuid=post_uuid
        )

    if not lang_code:
        return redirect("editor-urls:editor-lang-post-url",
                        post_uuid=str(post.uuid),
                        lang_code=lang_code if lang_code else Post.DEFAULT_LANGUAGE)

    view, created = EditedPostView.objects.get_or_create(
        source=post
    )
    view = EditedPostViewForm.update_form_preview(view, post)

    return render(request, 'editor/post.html', {
        "error": False,
        "status": "Success",
        "details": {
            "form": EditedPostViewForm(instance=view),
            "model": view,
            "markdown": formatted_markdown(view.markdown)
        }
    }, status=200)
