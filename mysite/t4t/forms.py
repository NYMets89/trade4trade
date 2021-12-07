from django import forms
from django.db.utils import OperationalError
from .models import Tag

class EditorForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    img_link = forms.URLField(required=True)
    body = forms.CharField(widget=forms.Textarea, required=True)
    choices = []

    def __init__(self):
        try:
            for tag in Tag.objects.all():
                self.choices.append((tag.tag_id, tag.name))
            tags = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=self.choices, required=True)
        except OperationalError:
            pass