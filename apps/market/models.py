from django.db import models
from mdeditor.fields import MDTextField
from djrichtextfield.models import RichTextField

from apps.core.models import BaseModel
from apps.core.utils import markdown_to_html


class Order(BaseModel):
    class Meta:
        abstract = False


class Category(BaseModel):
    class Meta:
        abstract = False

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default="",
        unique=True
    )
    slug = models.SlugField(
        max_length=255,
        null=False,
        blank=False,
        default="",
        allow_unicode=True,
        auto_created=True,
        unique=True
    )

    def __str__(self):
        return self.name


class Product(BaseModel):
    class Meta:
        abstract = False

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default="",
        unique=True
    )
    slug = models.SlugField(
        max_length=255,
        null=False,
        blank=False,
        default="",
        allow_unicode=True,
        unique=True
    )
    category = models.ForeignKey(
        "market.Category",
        on_delete=models.deletion.SET_NULL,
        null=True,
        blank=True,
        default=None
    )
    markdown_description = MDTextField(
        default=None,
        null=True,
        help_text="Markdown представление",
        blank=True
    )

    html_description = RichTextField(
        default=None,
        null=True,
        help_text="HTML представление",
        blank=True
    )

    def save(self, *args, **kwargs):
        self.html_description = markdown_to_html(str(self.markdown_description))
        return super(Product, self).save(*args, **kwargs)


class Seller(BaseModel):
    class Meta:
        abstract = False

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default="",
    )
