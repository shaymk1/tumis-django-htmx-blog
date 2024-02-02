from django.shortcuts import render
from .models import Post


def home_page(request):
    model = Post
    posts = Post.objects.all().order_by("-created_at")
    context = {"posts": posts, "model": model}
    return render(request, "blog/index.html", context)
