from django.db import models

from apps.core import mixins


class BaseModel(mixins.AutoincrementIDMixin,
                mixins.UUIDMixin,
                mixins.TimestampMixin,
                mixins.DefaultManagerMixin):
    class Meta:
        abstract = True

# class TestModel(BaseModel):
#     ...
