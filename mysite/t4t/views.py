from django.db.models.fields.related import ForeignKey
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import EditorForm, CommentForm
# Create your views here.

def home(request):
    return render(request=request, template_name='home.html')

def categorypage(request):
    category = Category.objects.all()
    return render(request=request, template_name='category.html', context={ 'category': category })

def skillspage(request, category_id):
    # get QuerySet object containing posts in descending order of post_id
    category = Category.objects.get(pk=category_id)
    posts = Post.objects.filter(category=category_id).order_by('-post_id')
    ####################tag = Tag.objects.get(pk=tag_id)


    if request.method == 'GET':
        form = EditorForm()
        return render(request=request, template_name='skills.html', context={ 'form': form, "posts": posts, "category":category})
    if request.method == 'POST':    
        # capture POST data as EditorForm instance
        form = EditorForm(request.POST)
        # validate form
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            post = Post.objects.create(title=title, body=body, category=category)
            ##############tag = Tag.objects.all()
            post.save()
            

        return redirect('skillspage', category_id=category.category_id)

def edit(request, post_id, category_id):
    
    if request.method == 'GET':
        # get Post object by its post_id
        post = Post.objects.get(pk=post_id)
        # get a list of tag_id from ManyRelatedManager object
        tags = []
        for tag in post.tags.all():
            tags.append(tag.tag_id)
        # pre-populate form with values of the post
        form = EditorForm(initial={ 'title': post.title, 'body': post.body})
        return render(request=request, template_name='edit.html', context={ 'form': form, 'post_id': post_id, 'category_id':category_id })
    if request.method == 'POST':    
        # capture POST data as EditorForm instance
        form = EditorForm(request.POST)
        # validate form
        if form.is_valid():
            # if form was submitted by clicking Save
            if 'save' in request.POST:
                # get cleaned data from form
                title = form.cleaned_data['title']
                body = form.cleaned_data['body']
                # filter QuerySet object by post_id
                posts = Post.objects.filter(pk=post_id)
                # update QuerySet object with cleaned title, body, img_link
                posts.update(title=title, body=body)
            # if form was submitted by clicking Delete
            elif 'delete' in request.POST:
                # filter QuerySet object by post_id and delete it
                Post.objects.filter(pk=post_id).delete()
        # redirect to 'blog/'
        return redirect('skillspage', category_id=category_id)

def create(request):
    if request.method == 'GET':
        form = EditorForm()
        return render(request=request, template_name='create.html', context={ 'form': form })
    if request.method == 'POST':    
        # capture POST data as EditorForm instance
        form = EditorForm(request.POST)
        # validate form
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            tags = form.cleaned_data['tags']
            post = Post.objects.create(title=title, body=body, tags=tags)
            post.tags.set(tags) 
            

        # redirect to 'blog/'
        return HttpResponseRedirect(reverse('home'))

def post_detail(request,post_id):
    post = Post.objects.get(post_id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', post_id=post.post_id)

    else:
        form = CommentForm()

    return render(request, "post_detail.html", {'post':post, 'form':form})