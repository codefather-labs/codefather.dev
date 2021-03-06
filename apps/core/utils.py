import sys
import base64
import os
import re
from enum import Enum
from typing import List, Union

from django.db.models import QuerySet
from django.utils.text import slugify
from mistletoe import HTMLRenderer, Document
from drf_yasg import openapi
from mistletoe.block_token import Heading
from mistletoe.span_token import RawText, Link, Strong, EscapeSequence
from pygments import highlight

from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name as get_lexer, guess_lexer
from pygments.styles import get_style_by_name as get_style

from settings.environment.base import DEFAULT_FRONTEND_THEME
from settings.environment.settings import get_settings_module
from apps.core.api.models import base_api_response

if sys.version_info < (3, 4):
    from mistletoe import _html as html
else:
    import html

settings = get_settings_module()


class Themes(Enum):
    MATERIAL = 'material'
    MONOKAI = 'monokai'
    SOLARIZED_DARK = 'solarized-dark'
    SOlARIZED_LIGHT = 'solarized-light'
    GRUVBOX_DARK = 'gruvbox-dark'
    DRACULA = 'dracula'
    ONE_DARK = 'one-dark'
    # ARDUINO = 'arduino' ?


base_code_style_theme = Themes.MONOKAI


class CustomHTMLFormatter(HtmlFormatter):
    def _wrap_pre(self, inner):
        style = []
        if self.prestyles:
            style.append(self.prestyles)
        if self.noclasses:
            style.append(self._pre_style)
        style.append("font-size: 16px")
        style = '; '.join(style)

        if self.filename and self.linenos != 1:
            yield 0, ('<span class="filename">' + self.filename + '</span>')

        # the empty span here is to keep leading empty lines from being
        # ignored by HTML parsers
        yield 0, ('<pre' + (style and ' style="%s"' % style) + '><span></span>')
        yield from inner
        yield 0, '</pre>'


class PygmentsRenderer(HTMLRenderer):
    formatter = CustomHTMLFormatter(style=base_code_style_theme.value)
    formatter.noclasses = True

    def __init__(self, *extras, style=base_code_style_theme.value, post_dir_path=None):
        super().__init__(*extras)
        self.post_dir_path = post_dir_path
        self.formatter.style = get_style(style)

    def render_heading(self, token: Heading):
        children: List[Union[RawText, Link, Strong, EscapeSequence]] = \
            token.children

        template = '<h{level} id={id}>{inner}</h{level}>'
        inner = ''.join(map(self.render, token.children))
        slug = slugify(inner, allow_unicode=True)
        return template.format(level=token.level, id=slug, inner=inner)

    def render_paragraph(self, token):
        if self._suppress_ptag_stack[-1]:
            return '{}'.format(self.render_inner(token))
        return '<p style="font-size: 16px;">{}</p>'.format(self.render_inner(token))

    def render_block_code(self, token):
        code = token.children[0].content
        lexer = get_lexer(token.language) if token.language else guess_lexer(code)
        "line-height: 125%; font-size: 16px"
        result = highlight(code, lexer, self.formatter)
        return result

    def render_image(self, token):
        template = '<center><img src="{}" alt="{}"{} /></center>'
        if token.title:
            title = ' title="{}"'.format(self.escape_html(token.title))
        else:
            title = ''

        src = "/%s" % "/".join(token.src.split("/")[1:])
        return template.format(src, self.render_to_plain(token), title)


def get_source_text(post_dir_path, filename: str) -> str:
    with open(f"{post_dir_path}/{filename}", 'r') as fin:
        with PygmentsRenderer(post_dir_path=post_dir_path) as renderer:
            # or: `with HTMLRenderer(AnotherToken1, AnotherToken2) as renderer:`

            doc = Document(fin)  # parse the lines into AST
            rendered = renderer.render(doc)  # render the AST
            # internal lists of tokens to be parsed are automatically reset when exiting this `with` block

    return rendered


def markdown_to_html(string: str):
    with PygmentsRenderer(post_dir_path=settings.BASE_DIR) as renderer:
        doc = Document(string)

    result = renderer.render(doc)

    if 'editor' in os.listdir(f"{settings.BASE_DIR}/media/"):
        editor_dir_path = f"{settings.BASE_DIR}/media/editor"
        os.system(f"rm -rf {editor_dir_path}")

    return result


def generate_api_response(
        success: bool,
        status: str = None,
        details_schema: openapi.Schema = None) -> base_api_response:
    return openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'error': openapi.Schema(
                type=openapi.TYPE_BOOLEAN, default=False if success else True
            ),
            'status': openapi.Schema(
                type=openapi.TYPE_STRING,
                default='Success' if success and not status else status if status else 'Failed',
            ),
            'details': details_schema if details_schema \
                else openapi.Schema(type=openapi.TYPE_OBJECT)
        })


def create_context(page_name: str, data=None):
    from apps.core.models import Post

    excluded_categories = ["Solution"]

    posts: QuerySet[Post] = Post.objects.filter(
        is_published=True,
    ).exclude(category__name__in=excluded_categories).order_by('-created_at')[:10]

    result = {
        "context": {
            "page": page_name,
        },
        "latest_posts": posts,
        "theme": DEFAULT_FRONTEND_THEME
    }
    if data:
        result['context'].update(**data)

    return result
