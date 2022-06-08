from django import forms
from django.contrib import admin
from djrichtextfield.widgets import RichTextWidget

from apps.core.models import Post, Tag, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)
    prepopulated_fields = {"slug": ("title",)}
    # form = PostForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)
