from django import forms
from mdeditor.fields import MDTextFormField

from apps.editor.models import EditedPostView


class EditedPostViewForm(forms.ModelForm):
    markdown = MDTextFormField()

    class Meta:
        model = EditedPostView
        fields = '__all__'
