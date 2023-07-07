from django.shortcuts import render, get_object_or_404

from .models import Post


def index_view(request): 
    posts = Post.objects.all().order_by("-created_at")
    context = {}
    context["posts"] = posts

    return render(request, "blog/index.html", context)


def search_view(request):
    if request.GET:
        query = request.GET.get("q")

        pass


def post_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {}
    context["post"] = post

    return render(request, "blog/post.html", context)