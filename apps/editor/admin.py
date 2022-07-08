from django.contrib import admin

from apps.editor.models import EditedPostView


@admin.register(EditedPostView)
class EditedPostViewAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)
