"""Module presenting the views funcitions for the blog application in this django project"""
from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag


def index(request):

    posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": posts})


def posts(request):
    try:
        posts = Post.objects.all()
        tags = Tag.objects.all()
    except LookupError:
        posts = None
        tags = None

    return render(request, "blog/all-posts.html", {
        "posts": posts,
        "tags": tags
    })


def post_details(request, slug):
    desired_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": desired_post,
        "tags": desired_post.tag.all()
    })


def explore_tags(request, caption):
    tag = Tag.objects.get(caption=caption)
    posts = Post.objects.filter(tag=tag)
    return render(request, "blog/tags.html", {
        "posts": posts,
        "tag": tag,
    })
