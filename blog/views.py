from django.shortcuts import render

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

