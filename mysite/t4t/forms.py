from django import forms
from .models import Tag, Comment

class EditorForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    body = forms.CharField(widget=forms.Textarea, required=True)
    choices = []
    tag = Tag.objects.all()
    for tag in Tag.objects.all():
        choices.append((tag.tag_id, tag.name))
    tags = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=choices, required=False)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'body']