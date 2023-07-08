from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Post


def index_view(request):
    posts = Post.objects.all().order_by('-created_at').prefetch_related('author')
    context = {
        'posts': posts,
    }

    return render(request, 'blog/index.html', context)


def search_view(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(Q(title__icontains=query)).all() \
                        .order_by('-created_at').prefetch_related('author')

    context = {
        'posts': posts,
        'search_query': query,
    }

    return render(request, 'blog/index.html', context)


def post_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }

    return render(request, 'blog/post.html', context)
