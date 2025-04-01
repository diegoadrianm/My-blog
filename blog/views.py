"""Module presenting the views funcitions for the blog application in this django project"""
from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag
from django.views.generic import ListView, DetailView


# def index(request):

#     posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {"posts": posts})

class IndexListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        base_query = super().get_queryset()
        top_3_query = base_query.order_by("-date")[:3]
        return top_3_query


# def posts(request):
#     try:
#         posts = Post.objects.all()
#         tags = Tag.objects.all()
#     except LookupError:
#         posts = None
#         tags = None

#     return render(request, "blog/all-posts.html", {
#         "posts": posts,
#         "tags": tags
#     })



class PostListView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context


# def post_details(request, slug):
#     desired_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-detail.html", {
#         "post": desired_post,
#         "tags": desired_post.tag.all()
#     })


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        post = get_object_or_404(Post, slug=self.kwargs["slug"])
        context = super().get_context_data(**kwargs)
        context["tags"] = post.tag.all()
        return context



# def explore_tags(request, caption):
#     tag = Tag.objects.get(caption=caption)
#     posts = Post.objects.filter(tag=tag)
#     return render(request, "blog/tags.html", {
#         "posts": posts,
#         "tag": tag,
#     })


class TagsListView(ListView):
    model = Post
    template_name = "blog/tags.html"
    context_object_name="posts"

    def get_queryset(self):
        base_queryset = super().get_queryset()
        tag = Tag.objects.get(caption=self.kwargs["caption"])
        filtered_tags = base_queryset.filter(tag=tag)
        return filtered_tags
