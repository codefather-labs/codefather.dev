import uuid

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render

from apps.editor.models import EditedPostView
from apps.editor.forms import EditedPostViewForm


@login_required(login_url='admin:login')
def editor(request: HttpRequest, edited_post_view_uuid: str = None):
    if request.method == "POST":
        form = EditedPostViewForm(request.POST)
        if form.is_valid():
            view = form.save()

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
            "status": "Form is not valid",
            "details": {
                "form": form,
            }
        }, status=200)

    is_exists = False
    if edited_post_view_uuid:
        is_exists = True

    if is_exists:
        try:
            view = EditedPostView.objects.get(uuid=edited_post_view_uuid)
        except EditedPostView.DoesNotExist:
            return render(request, 'editor/editor.html', {
                "error": True,
                "status": "View was not found",
                "details": {
                    "form": EditedPostViewForm,
                }
            }, status=404)

        return render(request, 'editor/editor.html', {
            "error": False,
            "status": "Success",
            "details": {
                "form": EditedPostViewForm(instance=view),
                "model": view
            }
        }, status=200)

    else:
        return render(request, 'editor/editor.html', {
            "error": False,
            "status": "Success",
            "details": {
                "form": EditedPostViewForm,
                "model": EditedPostView(uuid=str(uuid.uuid4()))
            }
        }, status=200)
