import json

from django.core.management import BaseCommand
from django.utils.text import slugify

from apps.core.models import Post, Tag
from settings.environment.settings import get_settings_module
from apps.core.utils import get_source_text

settings = get_settings_module()
BASE_DIR = settings.BASE_DIR


class Command(BaseCommand):
    # help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        post_dir_path = f"{BASE_DIR}/post"
        data = get_source_text(post_dir_path, 'article.md')

        query = {}
        with open(f'{post_dir_path}/data.json', 'r') as datafile:
            d = json.loads(datafile.read())
            query.update(d)

        query['body'] = data

        post = Post.objects.create(
            language=query['language'],
            author=query['author'],
            author_contact=query.get('author_contact'),
            title=query['title'],
            slug=slugify(query['title'], allow_unicode=True),
            body=query['body'],
        )

        [
            post.tags.add(
                Tag.objects.get_or_create(name=tag)[0]
            ) for tag in query['tags']
        ]

        post.save()
