from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.models import Post, Comment, Like
from main.user_form import SignUpForm
from main.login_form import LoginForm
from django.contrib.auth import login, authenticate


def index(request):
    posts = Post.objects.all()

    return render(request, "index.html", {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.all()


    return render(request, "post_detail.html", {'post': post, 'comments': comments})


def register(request):
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        form.save()

        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
        return redirect('/')

    return render(request, "register.html", {'form': form})


def log_in(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("/")

    return render(request, "login.html", {'form': form})


def account(request):
    return render(request, "account.html")