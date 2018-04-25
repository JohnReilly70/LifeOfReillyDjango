from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from . import password_gen
import logging

logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def blog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/blog.html', {'posts': posts})

def Secret_Area(request):
    return render(request, 'blog/Secret-Area.html', {})

# def password(request):
#     return render(request, 'blog/password_generator.html', {})

def password(request):
    logging.debug(1)
    if request.method == "POST":
        length = int(request.POST['length'])
        upper = int(request.POST['upper'])
        special = int(request.POST['special'])


        p = password_gen.password_gen(length,upper,special)
        context = {
            "password": p
        }
        print(p)
        return render(request, 'blog/password_generator.html', context)
    else:
        return  render(request, 'blog/password_generator.html')