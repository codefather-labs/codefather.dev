import os

from django.core.management import BaseCommand
from settings.environment.settings import get_settings_module

from apps.core.models import Post

settings = get_settings_module()
BASE_DIR = settings.BASE_DIR


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('post_dir', nargs='+', type=str)

    def handle(self, *args, **options):
        post_dir = options['post_dir'][0]
        post_file = ""

        for file in os.listdir(post_dir):
            if file[-3:] == '.md':
                post_file = file

        post_text = open(f"{post_dir}/{post_file}", 'r').read()

        path = lambda x, y: f"{x}/media/{y}/"
        os.system(f"mkdir media/post")
        os.system(f"mkdir {path(settings.BASE_DIR, post_dir)}")

        for file in os.listdir(post_dir):
            if file[-3:] not in ('.md', '.DS_Store'):
                # image_file_path = path(settings.BASE_DIR, f"{post_dir}/{file}")
                image_file_path = f"{settings.HOST}/media/{post_dir}/{file}"
                post_text = post_text.replace(
                    file, image_file_path
                )

                command = f"cp -r {post_dir}/{file} {settings.BASE_DIR}/media/{post_dir}/"
                os.system(command)

        Post.objects.create(
            title="Python Internals",
            slug="python-internals",
            markdown=post_text,
        )
