from django.contrib import admin

from apps.market import models


@admin.register(models.Seller)
class SellerAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'uuid')


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'category', 'markdown_description')
    readonly_fields = ('id', 'uuid')
    prepopulated_fields = {"slug": ("name",)}

    list_display = ('id', 'name', 'category')
    list_display_links = ('name', 'id')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    exclude = ('uuid',)
    prepopulated_fields = {"slug": ("name",)}

    list_display = ('id', 'name', 'uuid')
    list_display_links = ('name', 'id')
