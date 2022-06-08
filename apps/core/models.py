from django.db import models
from mdeditor.fields import MDTextField
from djrichtextfield.models import RichTextField

from apps.core import mixins
from apps.core.utils import markdown_to_html


class BaseModel(mixins.AutoincrementIDMixin,
                mixins.UUIDMixin,
                mixins.TimestampMixin,
                mixins.DefaultManagerMixin):
    class Meta:
        abstract = True


class Tag(BaseModel):
    name = models.CharField(
        max_length=255,
        default=None,
        null=True
    )

    def __str__(self):
        return str(self.name)


class Category(BaseModel):
    name = models.CharField(
        max_length=255,
        default=None,
        null=True
    )

    def __str__(self):
        return str(self.name)


class Post(BaseModel):
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
        null=True,
        help_text="Markdown представление",
        blank=True
    )

    body = RichTextField(
        default=None,
        null=False,
        help_text="HTML представление",
        blank=True
    )
    tags = models.ManyToManyField(
        "core.Tag",
        default=None,
        blank=True,
    )

    category = models.ForeignKey(
        "core.Category",
        on_delete=models.deletion.SET_NULL,
        default=None,
        blank=True,
        null=True
    )

    author = models.CharField(
        max_length=255,
        default=None,
        null=True
    )
    author_contact = models.CharField(
        max_length=255,
        default=None,
        null=True
    )

    is_comments_available = models.BooleanField(
        default=True,
        null=True,
    )

    is_already_formatted = models.BooleanField(
        default=False,
        null=True,
    )

    def save(self, *args, **kwargs):
        if not self.is_already_formatted:
            self.body = markdown_to_html(str(self.markdown))
            self.is_already_formatted = True
        return super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}, {self.author}"
