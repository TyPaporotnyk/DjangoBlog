from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=1000, blank=True, null=True)

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    slug = models.SlugField(default="", null=False, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
