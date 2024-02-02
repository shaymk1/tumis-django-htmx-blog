from django.shortcuts import render
from .models import Post


def index(request):
    model = Post
    posts = Post.objects.all().order_by("-created_at")
    context = {"posts": posts, "model": model}
    return render(request, "blog/index.html", context)


def article(request):
    return render(request, "blog/article.html")


def articles(request):
    return render(request, "blog/articles.html")
