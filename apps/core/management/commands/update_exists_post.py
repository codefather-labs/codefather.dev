import os
from typing import Optional

from django.core.management import BaseCommand
from django.db.models import QuerySet
from django.utils.text import slugify

from settings.environment.settings import get_settings_module

from apps.core.models import Post

settings = get_settings_module()
BASE_DIR = settings.BASE_DIR


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('post_file', nargs='+', type=str)

    def handle(self, *args, **options):
        post_file = options['post_file'][0]
        post_name = "".join(str(post_file)
                            .rsplit("/", maxsplit=1)[-1]
                            .split(".")[:-1]) \
            .replace("_", " ")
        print(post_name)
        post_dir = "/".join(str(post_file).split("/")[:-1])

        with open(f"{post_file}", 'r', encoding='utf-8') as p_file:
            post_text = p_file.read()

        path = lambda x, y: f"{x}/media/{y}/"
        os.system("mkdir media/post")
        os.system(f"mkdir {path(settings.BASE_DIR, post_dir)}")

        for file in os.listdir(post_dir):
            if file[-3:] not in ('.md', '.DS_Store'):
                # image_file_path = path(settings.BASE_DIR, f"{post_dir}/{file}")
                image_file_path = f"{settings.HOST}/media/{post_dir}/{file}"
                post_text = post_text.replace(file, image_file_path)

                command = f"cp -r {post_dir}/{file} {settings.BASE_DIR}/media/{post_dir}/"
                os.system(command)

        post: QuerySet[Post] = Post.objects.filter(
            title=post_name
        )
        if post:
            post: Post = post.last()

            post.markdown = post_text
            post.is_already_formatted = False
            post.save()
