# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, redirect
from forms import SignUpForm, LoginForm
from models import UserModel, SessionToken
from django.contrib.auth.hashers import make_password, check_password

def signup_view(request):
    if request.method == "POST":
        print "Sign up form submitted"
        form = SignUpForm(request.POST)
        if form.is_valid():
            print "form is valid"
            username = form.cleaned_data["username"]
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            print username+ ":"+ name+ ":"+ email+ ":"+ password+ ":"+ make_password(password)
            user = UserModel(name=name, password=make_password(password), email=email, username=username)
            user.save()
            return render(request, "success.html")
        else:
            print "invalid form"
    elif request.method == "GET":
        form = SignUpForm()
        today = datetime.now()
        return render(request, "index.html", {"form" : form, "today":today})


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
                    response = redirect("feed/")
                    response.set_cookie(key="session_token", value=token.session_token)
                    return response
                else:
                    print "Incorrect password"
            else:
                print "username is invalid"

    elif request.method == "GET":
        form = LoginForm()

    return render(request, "login.html", {"form": form})

def feed_view(request):
    return render(request, "feed.html")

def check_validation(request):
    if request.COOKIES.get("session_token"):
        session = SessionToken.objects.filter(session_token=request.COOKIES.get("session_token")).first()
        if session:
           return session.user
    else:
        return None