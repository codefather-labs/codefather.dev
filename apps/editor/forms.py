from django import forms
from django.forms.utils import flatatt
from django.template.loader import render_to_string
from django.utils.encoding import force_str
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from mdeditor.configs import MDConfig
from mdeditor.fields import MDTextFormField
from mdeditor.widgets import MDEditorWidget

from apps.core.models import Post
from apps.editor.models import EditedPostView


class CustomMDEditorWidget(MDEditorWidget):
    """
        Widget providing Editor.md for Rich Text Editing.
        see Editor.md docs: https://pandao.github.io/editor.md/examples/index.html
        """

    def __init__(self, config_name='default', *args, **kwargs):
        super(MDEditorWidget, self).__init__(*args, **kwargs)
        # Setup config from defaults.
        self.config = MDConfig(config_name)

    def render(self, name, value, renderer=None, attrs=None):
        """
        renderer: django2.1 新增加的参数，此处不做应用，赋值None做兼容处理
        """
        if value is None:
            value = ''

        final_attrs = self.build_attrs(self.attrs, attrs, name=name)
        res = mark_safe(render_to_string('markdown.html', {
            'final_attrs': flatatt(final_attrs),
            'value': conditional_escape(force_str(value)),
            'id': final_attrs['id'],
            'config': self.config,
        }))
        return res

    def build_attrs(self, base_attrs, extra_attrs=None, **kwargs):
        """
        Helper function for building an attribute dictionary.
        This is combination of the same method from Django<=1.10 and Django1.11+
        """
        attrs = dict(base_attrs, **kwargs)
        if extra_attrs:
            attrs.update(extra_attrs)
        return attrs

    def _get_media(self):
        return forms.Media(
            css={
                "all": ("mdeditor/css/editormd.css",)
            },
            js=(
                "mdeditor/js/jquery.min.js",
                "mdeditor/js/editormd.min.js",
            ))

    media = property(_get_media)


class CustomMDTextFormField(forms.fields.CharField):
    """ custom form field """

    def __init__(self, config_name='default', *args, **kwargs):
        kwargs.update({
            'widget': CustomMDEditorWidget(config_name=config_name)
        })
        super(CustomMDTextFormField, self).__init__(*args, **kwargs)


class EditedPostViewForm(forms.ModelForm):
    # uuid = forms.CharField()
    markdown = CustomMDTextFormField()
    # source = forms.ModelChoiceField(queryset=Post.objects.all())
    slug = forms.SlugField(required=False, allow_unicode=True)
    title = forms.CharField(required=True)
    language = forms.CharField(required=True)

    class Meta:
        model = EditedPostView
        fields = '__all__'
        exclude = ('uuid', 'source')

    @staticmethod
    def update_form_preview(instance: EditedPostView, post: Post):
        if not instance.slug:
            instance.slug = post.slug

        if not instance.title:
            instance.title = post.title

        if not instance.markdown:
            instance.markdown = post.markdown

        return instance

    @staticmethod
    def swap_delimiters(string: str):
        string = string.replace("$//$", "\n")
        string = string.replace("$ //$", "\n")
        string = string.replace("$// $", "\n")
        string = string.replace("$ // $", "\n")
        return string
