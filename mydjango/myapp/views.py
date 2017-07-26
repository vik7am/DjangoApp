# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, redirect, render_to_response
from forms import SignUpForm, LoginForm, PostForm, LikeForm, CommentForm
from models import UserModel, SessionToken, PostModel, LikeModel, CommentModel
from django.contrib.auth.hashers import make_password, check_password
from imgurpython import ImgurClient
from mydjango.settings import BASE_DIR
from django.contrib import messages


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            print "form is valid"
            username = form.cleaned_data["username"]
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            #user = UserModel(name=name, password=make_password(password), email=email, username=username)
            #user.save()
            print "Id created"
            return render(request, "index.html", {"form": form, "error": "Id Created"})
            #return redirect("/login/")
        else:
            print "invalid form"
            return render(request, "index.html", {"form": form,"error": "Invalid data"})
    elif request.method == "GET":
        form = SignUpForm()
        return render(request, "index.html", {"form" : form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = UserModel.objects.filter(username=username).first()
            if user:
                if check_password(password, user.password):
                    token = SessionToken(user=user)
                    token.create_token()
                    token.save()
                    print "Welcome"
                    response = redirect("/feed/")
                    response.set_cookie(key="session_token", value=token.session_token)
                    return response
                else:
                    print "Incorrect password"
                    return render(request, "login.html", {"form": form, "error": "Invalid password"})
            else:
                print "username is invalid"
                return render(request, "login.html", {"form": form,"error":"Invalid username"})
    elif request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})


def check_validation(request):
    if request.COOKIES.get("session_token"):
        session = SessionToken.objects.filter(session_token=request.COOKIES.get("session_token")).first()
        if session:
           return session.user
    else:
        return None


def post_view(request):
    user = check_validation(request)
    if user:
        if request.method == 'GET':
            form = PostForm()
        elif request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                image = form.cleaned_data.get('image')
                caption = form.cleaned_data.get('caption')
                post = PostModel(user=user, image=image, caption=caption)
                path = str(BASE_DIR +"/user_images/"+ post.image.url)
                post.save()
                client = ImgurClient("48b3c07ebcf5ecb", "af316e94ac2544c61623ed0fe4a80f2ce928ce33")
                post.image_url = client.upload_from_path(path, anon=True)['link']
                post.save()
                return redirect('/feed/')
        return render(request, 'post.html', {'form': form})
    else:
        return redirect('/login/')


def feed_view(request):
    user = check_validation(request)
    if user:
        posts = PostModel.objects.all().order_by('-created_on')
        for post in posts:
            existing_like = LikeModel.objects.filter(post_id=post.id, user=user).first()
            if existing_like:
                post.has_liked = True
        return render(request, 'feed.html', {'posts': posts})
    else:
        return redirect('/login/')


def like_view(request):
    user = check_validation(request)
    if user and request.method == 'POST':
        form = LikeForm(request.POST)
        if form.is_valid():
            post_id = form.cleaned_data.get('post').id
            existing_like = LikeModel.objects.filter(post_id=post_id, user=user).first()
            if not existing_like:
                LikeModel.objects.create(post_id=post_id, user=user)
            else:
                existing_like.delete()
            return redirect('/feed/')
    else:
        return redirect('/login/')


def comment_view(request):
    user = check_validation(request)
    if user and request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = form.cleaned_data.get('post').id
            comment_text = form.cleaned_data.get('comment_text')
            CommentModel.objects.create(user=user, post_id=post_id, comment_text=comment_text)
            return redirect('/feed/')
        else:
            return redirect('/feed/')
    else:
        return redirect('/login')