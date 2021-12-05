from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import EditorForm
# Create your views here.

def home(request):
    # get QuerySet object containing posts in descending order of post_id
    return render(request=request, template_name='home.html')