from django.contrib import admin

from apps.core.models import Post, Tag, Category, PostMetaTag


class PostMetaTagInline(admin.TabularInline):
    model = PostMetaTag
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', 'get_absolute_url')
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'author', 'uuid')


    inlines = (PostMetaTagInline,)

    fieldsets = (
        ("Post", {
            'fields': (
                'title', 'slug', 'language',
                'category', 'tags', 'author',
                'author_contact', 'is_comments_available',
                'is_already_formatted', 'is_published', 'is_isolated'
            )
        }),
        # ("Editors", {
        #     'classes': ('collapse',),
        #     'fields': ('markdown', 'body'),
        # }),
        ('Metadata', {
            # 'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description', 'get_absolute_url'),
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)
    prepopulated_fields = {"slug": ("name",)}
