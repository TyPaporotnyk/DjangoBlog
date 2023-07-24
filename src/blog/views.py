from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import (
    Post,
    Tag,
)


def index_view(request):
    posts = Post.objects.all().order_by('-created_at') \
                        .prefetch_related('author').prefetch_related('tags')
    tags = Tag.objects.all()

    context = {
        'posts': posts,
        'tags': tags,
    }

    return render(request, 'blog/index.html', context)


def search_view(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(Q(title__icontains=query)).all().order_by('-created_at') \
                        .prefetch_related('author').prefetch_related('tags')
    tags = Tag.objects.all()

    context = {
        'posts': posts,
        'search_query': query,
        'tags': tags,
    }

    return render(request, 'blog/index.html', context)


def category_view(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag).all().order_by('-created_at') \
                        .prefetch_related('author').prefetch_related('tags')
    tags = Tag.objects.all()

    context = {
        'posts': posts,
        'tags': tags,
        'selected_tag': tag,
    }

    return render(request, 'blog/index.html', context)


def post_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }

    return render(request, 'blog/post.html', context)
