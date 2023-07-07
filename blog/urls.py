from django.urls import path

from . import views


urlpatterns = [
    path("", views.index_view, name="home"),
    path("search/", views.search_view, name="search"),
    path("<slug:slug>/", views.post_view, name="post")
]
