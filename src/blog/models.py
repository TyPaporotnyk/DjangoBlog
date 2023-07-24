from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=1000, blank=True, null=True)

    content = RichTextField(blank=True, null=True)

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    slug = models.SlugField(default='', null=False, unique=True)

    tags = models.ManyToManyField('Tag', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    slug = models.SlugField(default='', unique=True, null=False)

    def __str__(self) -> str:
        return self.name
