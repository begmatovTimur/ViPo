from django.shortcuts import render, redirect
from main.models import Post
from main.user_form import SignUpForm
from django.contrib.auth import login, authenticate


def index(request):
    posts = Post.objects.all()

    return render(request, "index.html", {'posts': posts})


def register(request):
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, "register.html", {'form': form})