from django.contrib.sitemaps import Sitemap
from django.core.paginator import Paginator, Page
from django.urls import reverse

from apps.core.models import Post, Category, Tag
from settings.environment.settings import get_settings_module, environment

settings = get_settings_module()
DEFAULT_PROTOCOL_STRATEGY = 'https' \
    if environment.value == 'Production' else 'http'


class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = DEFAULT_PROTOCOL_STRATEGY

    def items(self):
        return [
            'core-urls:main_url',
            'core-urls:resume_url',
            'core-urls:projects_url',
            'core-urls:blog_url',
            'core-urls:contacts_url',
        ]

    def location(self, item):
        return reverse(item)


class CategorySitemap(Sitemap):
    changefreq = "dayly"
    priority = 0.5
    protocol = DEFAULT_PROTOCOL_STRATEGY

    def items(self):
        return Category.objects.all().order_by('-created_at')

    def lastmod(self, obj: Category):
        return obj.updated_at

    def location(self, item: Category):
        return item.get_absolute_url()


class TagSitemap(Sitemap):
    changefreq = "dayly"
    priority = 0.5
    protocol = DEFAULT_PROTOCOL_STRATEGY

    def items(self):
        return Tag.objects.all().order_by('-created_at')

    def lastmod(self, obj: Tag):
        return obj.updated_at

    def location(self, item: Tag):
        return item.get_absolute_url()


class PostSitemap(Sitemap):
    changefreq = "dayly"
    priority = 0.5
    protocol = DEFAULT_PROTOCOL_STRATEGY

    def items(self):
        return Post.objects.filter(is_published=True).order_by('-created_at')

    def lastmod(self, obj: Post):
        return obj.updated_at

    def location(self, item: Post):
        return item.get_absolute_url()

    # @cached_property
    # def paginator(self):
    #     return Paginator(object_list=list(self.items()), per_page=50)
