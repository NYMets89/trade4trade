from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title =  models.CharField(max_length=255)
    # intro = models.TextField(default=' ')
    body = models.TextField()
    # date_added= models.DateTimeField(auto_now_add=True, default)
    tags = models.ManyToManyField(Tag)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, default= ' ')
    def __unicode__(self):
       return 'Post: ' + self.name

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, default= ' ')
    comment = models.CharField(max_length=255)
    email = models.EmailField(default= ' ')
    body = models.TextField(default=' ')