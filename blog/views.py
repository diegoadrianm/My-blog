from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/all-posts.html")


def post_details(request):
    pass