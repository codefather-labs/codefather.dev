from django.db import models

from apps.core.models import BaseModel


class Order(BaseModel):
    class Meta:
        abstract = False

    ...


class Product(BaseModel):
    class Meta:
        abstract = False

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default="",
    )
    slug = models.SlugField(
        max_length=255,
        null=False,
        blank=False,
        default="",
        allow_unicode=True
    )


class Seller(BaseModel):
    class Meta:
        abstract = False

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default="",
    )
