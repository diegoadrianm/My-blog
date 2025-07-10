from django.urls import path
from . import views
urlpatterns = [
    path("", views.IndexListView.as_view(), name='blog-index'),
    path("posts", views.PostListView.as_view(), name='blog-posts'),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name='blog-post-details'),
    path("posts/tags/<str:caption>", views.TagsListView.as_view(), name="tags")
]
