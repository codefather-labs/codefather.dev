from abc import abstractmethod

from django.db import models


class PageHeadMetaTagMixin(models.Model):
    class Meta:
        abstract = True

    __META_NAME = 'name'
    __META_PROPERTY = 'property'
    __META_CHARSET = 'charset'
    __META_HTTP_EQUIV = 'http-equiv'
    __META_TYPES = (
        (__META_NAME, __META_NAME),
        (__META_PROPERTY, __META_PROPERTY),
        (__META_CHARSET, __META_CHARSET),
        (__META_HTTP_EQUIV, __META_HTTP_EQUIV)
    )
    meta_tag_type = models.CharField(
        max_length=255,
        default=None,
        null=False,
        blank=False,
        choices=__META_TYPES
    )

    meta_tag_key = models.CharField(
        max_length=255,
        default=None,
        null=False,
        blank=False
    )
    meta_tag_content = models.CharField(
        max_length=255,
        default=None,
        null=True,
        blank=True
    )

    meta_model = models.ForeignKey(
        "meta.PageHeadMixin",
        related_name='meta_tags',
        on_delete=models.deletion.CASCADE,
        default=None,
        null=False,
        blank=False
    )

    @property
    def render(self):
        format_dict = {
            "type": self.meta_tag_type,
            "key": self.meta_tag_key
        }
        pattern = "<meta {type}={key}>"

        if self.meta_tag_content:
            pattern = "<meta {type}={key} content={content}>"
            format_dict['content'] = self.meta_tag_content

        return pattern.format(**format_dict)


class PageHeadMixin(models.Model):
    class Meta:
        abstract = True

    DEFAULT_PAGE_TITLE = 'codefather.dev - Software developers community'

    meta_title = models.CharField(
        max_length=255,
        default=None,
        null=True,
        blank=True
    )

    meta_description = models.CharField(
        max_length=255,
        default=None,
        null=True,
        blank=True
    )

    @property
    def render_meta_title(self):
        return f"<title>{self.meta_title}</title>"

    @property
    def render_meta_description(self):
        return f'<meta name="description" content="{self.meta_description}">'

    @property
    def meta_tags_list(self):
        return self.meta_tags.all()

    @property
    def render_all_metadata(self):
        result = [self.render_meta_title, self.render_meta_description] + [
            tag.render for tag in self.meta_tags_list
        ]

        return "\n".join(result)

    @abstractmethod
    def get_absolute_url(self) -> str: ...

    @property
    @abstractmethod
    def url_pattern(self) -> str: ...
