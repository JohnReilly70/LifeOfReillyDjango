from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def blog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/blog.html', {'posts': posts})

def Secret_Area(request):
    return render(request, 'blog/Secret-Area.html', {})

def password(request):
    return render(request, 'blog/password_generator.html', {})