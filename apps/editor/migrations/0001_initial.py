# Generated by Django 4.0.5 on 2022-07-23 10:18

import apps.core.mixins
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditedPostView',
            fields=[
                ('id', models.PositiveBigIntegerField(db_index=True, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True, validators=[django.core.validators.RegexValidator('^[0-9A-F]{8}-[0-9A-F]{4}-[4][0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$')])),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('language', models.CharField(blank=True, default='ru', max_length=255, null=True)),
                ('title', models.CharField(blank=True, db_index=True, default=None, max_length=255, null=True)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, default=None, max_length=255, null=True)),
                ('markdown', mdeditor.fields.MDTextField(blank=True, default=None, help_text='Markdown представление', null=True)),
                ('source', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.post')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, apps.core.mixins.DefaultManagerMixin),
        ),
    ]
