from django.contrib.sitemaps import ping_google
from django.db import models
from django.urls import reverse
from mdeditor.fields import MDTextField
from djrichtextfield.models import RichTextField

from apps.core import mixins
from apps.core.utils import markdown_to_html
from apps.meta.models import PageHeadMetaTagMixin, PageHeadMixin
from settings.environment.settings import get_settings_module, environment

settings = get_settings_module()


class BaseModel(mixins.AutoincrementIDMixin,
                mixins.UUIDMixin,
                mixins.TimestampMixin,
                mixins.DefaultManagerMixin):
    class Meta:
        abstract = True


class Tag(BaseModel):
    class Meta:
        abstract = False

    name = models.CharField(
        max_length=255,
        default=None,
        null=True
    )
    slug = models.SlugField(
        max_length=255,
        db_index=True,
        default=None,
        null=True,
        blank=True,
        allow_unicode=True
    )

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("core-urls:tag_url", kwargs={
            "reference": self.slug
        })


class Category(BaseModel):
    class Meta:
        abstract = False

    name = models.CharField(
        max_length=255,
        default=None,
        null=True
    )
    slug = models.SlugField(
        max_length=255,
        db_index=True,
        default=None,
        null=True,
        blank=True,
        allow_unicode=True
    )

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("core-urls:category_url", kwargs={
            "reference": self.slug
        })


class PostMetaTag(PageHeadMetaTagMixin):
    class Meta:
        abstract = False

    meta_model = models.ForeignKey(
        "core.Post",
        related_name='meta_tags',
        on_delete=models.deletion.CASCADE,
        default=None,
        null=False,
        blank=False
    )


class Post(BaseModel, PageHeadMixin):
    class Meta:
        abstract = False

    DEFAULT_LANGUAGE = 'en'
    language = models.CharField(
        max_length=255,
        default='ru',
        null=True,
        blank=True
    )

    title = models.CharField(
        max_length=255,
        default=None,
        null=True,
        blank=True,
        db_index=True
    )

    slug = models.SlugField(
        max_length=255,
        db_index=True,
        default=None,
        null=True,
        blank=True,
        allow_unicode=True
    )

    markdown = MDTextField(
        default=None,
        null=True,
        help_text="Markdown представление",
        blank=True
    )

    body = RichTextField(
        default=None,
        null=True,
        help_text="HTML представление",
        blank=True
    )
    tags = models.ManyToManyField(
        "core.Tag",
        default=None,
        blank=True,
    )

    category = models.ForeignKey(
        "core.Category",
        on_delete=models.deletion.SET_NULL,
        default=None,
        blank=True,
        null=True
    )
    author = models.CharField(
        max_length=255,
        default=None,
        null=True,
        blank=True
    )
    author_contact = models.CharField(
        max_length=255,
        default=None,
        null=True,
        blank=True
    )

    is_comments_available = models.BooleanField(
        default=True,
        null=True,
        blank=True
    )

    is_already_formatted = models.BooleanField(
        default=False,
        null=True,
        blank=True
    )

    is_published = models.BooleanField(
        default=False,
        null=True,
        blank=True
    )

    is_isolated = models.BooleanField(
        default=False,
        null=True,
        blank=True
    )

    @property
    def render_meta_title(self):
        if not self.meta_title:
            return f"<title>{self.title} by {self.author} at codefather.dev</title>" \
                if self.author else f"<title>{self.title} at codefather.dev</title>"
        return f"<title>{self.meta_title}</title>"

    @property
    def render_meta_description(self):
        if self.meta_description:
            return f'<meta name="description" content="{self.meta_description}">'
        return ""

    @property
    def url_pattern(self):
        return "core-urls:post_url"

    def get_absolute_url(self):
        return reverse(self.url_pattern, kwargs={
            "reference": self.slug
        })

    def save(self, *args, **kwargs):
        if not self.language:
            self.language = self.DEFAULT_LANGUAGE

        if not self.is_already_formatted:
            self.body = markdown_to_html(str(self.markdown))
            self.is_already_formatted = True

        if environment.value == 'Production':
            # TODO add pinging log
            try:
                ping_google()
            except Exception:
                # Bare 'except' because we could get a variety
                # of HTTP-related exceptions.
                pass

        return super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

    @property
    def glitch_title(self):
        splited = str(self.title).split(' ')
        result = []
        buf = []
        to_html = lambda x: '<div ' \
                            'class="blog_title glitch-effect" ' \
                            'data-text="%s">%s</div>' % (x, x)
        while splited:
            item = splited.pop(0)
            buf_len = len(" ".join(buf))
            if len(item) + buf_len < 20:
                buf.append(item)

            else:
                result.append(to_html(" ".join(buf)))
                buf.clear()
                buf.append(item)

        else:
            if buf:
                result.append(to_html(" ".join(buf)))
                buf.clear()

        return """
        <div class="h-title blog_title">
            %s
        </div>
        """ % "\n".join(result)
