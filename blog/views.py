"""Module presenting the views funcitions for the blog application in this django project"""
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View, ListView
from .models import Post, Tag
from .forms import CommentForm


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


class PostDetailView(View):

    def get(self, request, slug):
        desired_post = get_object_or_404(Post, slug=slug)
        context = {
            "post": desired_post,
            "tags": desired_post.tag.all(),
            "comment_form": CommentForm(),
            "comments": desired_post.comments.all().order_by("-id")
        }
        return render(request, "blog/post_detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        desired_post = get_object_or_404(Post, slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = desired_post
            comment.save()

            return HttpResponseRedirect(reverse("blog-post-details", args=[slug]))
        context = {
            "post": desired_post,
            "tags": desired_post.tag.all(),
            "comment_form": CommentForm(),
            "comments": desired_post.comments.all()
        }
        return render(request, "blog/post_detail.html", context)


class TagsListView(ListView):
    model = Post
    template_name = "blog/tags.html"
    context_object_name = "posts"

    def get_queryset(self):
        base_queryset = super().get_queryset()
        tag = Tag.objects.get(caption=self.kwargs["caption"])
        filtered_tags = base_queryset.filter(tag=tag)
        return filtered_tags
