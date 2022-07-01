from django.db import models
from mdeditor.fields import MDTextField

from apps.core import mixins


class EditedPostView(mixins.AutoincrementIDMixin,
                     mixins.UUIDMixin,
                     mixins.TimestampMixin,
                     mixins.DefaultManagerMixin):
    language = models.CharField(
        max_length=255,
        default='ru',
        null=False,
    )

    title = models.CharField(
        max_length=255,
        default=None,
        null=False,
        db_index=True
    )

    slug = models.SlugField(
        max_length=255,
        db_index=True,
        default=None,
        null=True,
        allow_unicode=True
    )

    markdown = MDTextField(
        default=None,
        null=False,
        help_text="Markdown представление",
        blank=True
    )

    source = models.ForeignKey(
        "core.Post",
        on_delete=models.deletion.SET_NULL,
        default=None,
        null=True,
        blank=True
    )

    def __str__(self):
        return "%s, %s" % (self.language, self.title)
