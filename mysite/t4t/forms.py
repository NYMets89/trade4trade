from django import forms
from django.db.utils import OperationalError
from django.forms import fields
from .models import Tag, Comment

class EditorForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    img_link = forms.URLField(required=True)
    body = forms.CharField(widget=forms.Textarea, required=True)
    choices = []

    def __init__(self):
        try:
            for tag in Tag.objects.all():
                self.choices.append((tag.tag_id, tag.name))
            tag = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=self.choices, required=True)
        except OperationalError:
            pass

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'email', 'body']