from django import forms
from .models import Tag, Comment
from django.db.utils import OperationalError

class EditorForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    body = forms.CharField(widget=forms.Textarea, required=True)
    choices = []
    try:
        tag = Tag.objects.all()
        for tag in Tag.objects.all():
            choices.append((tag.tag_id, tag.name))
        tags = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=choices, required=False)
    except OperationalError:
        pass  # happens when db doesn't exist yet, views.py should be
            # importable without this side effect

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'body']