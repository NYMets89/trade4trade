from django import forms
from django.db.utils import OperationalError
from django.forms import fields
from .models import Tag, Comment

class EditorForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    body = forms.CharField(widget=forms.Textarea, required=True)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'email', 'body']