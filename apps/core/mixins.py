import uuid as uuid
from django.core.validators import RegexValidator
from django.db import models
from datetime import datetime


class DefaultManagerMixin:
    DoesNotExist = models.ObjectDoesNotExist

    objects = models.Manager()


class AutoincrementIDMixin:
    id = models.PositiveBigIntegerField(
        primary_key=True, null=False, blank=False, db_index=True,
    )


class UUIDMixin(models.Model):
    uuid = models.UUIDField(
        null=False, blank=False, db_index=True,
        default=uuid.uuid4, unique=True, validators=[
            RegexValidator(
                '^[0-9A-F]{8}-[0-9A-F]{4}-[4][0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$'
            )
        ]
    )

    class Meta:
        abstract = True


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, null=True
    )

    updated_at = models.DateTimeField(
        auto_now=True, null=True
    )

    @property
    def clear_created_date(self):
        self.created_at: datetime
        return self.created_at.strftime("%d.%m.%Y, %H:%M:%S")

    @property
    def clear_updated_date(self):
        self.updated_at: datetime
        return self.updated_at.strftime("%d.%m.%Y, %H:%M:%S")

    class Meta:
        abstract = True
