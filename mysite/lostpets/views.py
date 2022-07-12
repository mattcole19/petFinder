from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Post


# Create your views here.
def index(request):
    return render(request, 'lostpets/index.html')


# Shows 5 most recent posts
def home(request):
    latest_posts = Post.objects.all()
    context = {"posts": latest_posts}
    return render(request, 'lostpets/home.html', context)


# Shows full information for that post
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'lostpets/post.html', {'post': post})
