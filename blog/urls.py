from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='blog-index'),
    path("posts", views.posts, name='blog-posts'),
    path("posts/<slug:slug>", views.post_details, name='blog-post-details'),
    path("posts/tags/<str:caption>", views.explore_tags, name="tags")
]
