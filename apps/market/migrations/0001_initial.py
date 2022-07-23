# Generated by Django 4.0.5 on 2022-07-23 12:55

import apps.core.mixins
import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.PositiveBigIntegerField(db_index=True, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True, validators=[django.core.validators.RegexValidator('^[0-9A-F]{8}-[0-9A-F]{4}-[4][0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$')])),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, apps.core.mixins.DefaultManagerMixin),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.PositiveBigIntegerField(db_index=True, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True, validators=[django.core.validators.RegexValidator('^[0-9A-F]{8}-[0-9A-F]{4}-[4][0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$')])),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(default='', max_length=255)),
                ('slug', models.SlugField(allow_unicode=True, default='', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, apps.core.mixins.DefaultManagerMixin),
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.PositiveBigIntegerField(db_index=True, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True, validators=[django.core.validators.RegexValidator('^[0-9A-F]{8}-[0-9A-F]{4}-[4][0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$')])),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(default='', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, apps.core.mixins.DefaultManagerMixin),
        ),
    ]