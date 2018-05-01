from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import login, authenticate, decorators

from .models import Post
from . import password_gen
from .forms import SignUpForm

import logging

logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def blog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/blog.html', {'posts': posts})

@decorators.login_required
def Secret_Area(request):
    return render(request, 'blog/Secret-Area.html', {})

# def password(request):
#     return render(request, 'blog/password_generator.html', {})

def password(request):
    if request.method == "POST":
        length = int(request.POST['length'])
        upper = int(request.POST['upper'])
        special = int(request.POST['special'])


        p = password_gen.password_gen(length,upper,special)
        context = {
            "password": p
        }
        return render(request, 'blog/password_generator.html', context)
    else:
        return  render(request, 'blog/password_generator.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            cheese = form.cleaned_data.get('cheese')
            user = authenticate(username=username, password=raw_password, cheese=cheese)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})