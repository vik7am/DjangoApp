# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render
from forms import SignUpForm, LoginForm
from django.contrib.auth.hashers import make_password

def signup_view(request):
    if request.method == "POST":
        print 'Sign up form submitted'
        form = SignUpForm(request.POST)
        if form.is_valid():
            print "form is valid"
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print username+ ":"+ name+ ":"+ email+ ":"+ password+ ":"+ make_password(password)
            return render(request, 'success.html')
        else:
            print "invalid form"
    elif request.method == 'GET':
        form = SignUpForm()
        today = datetime.now()
        return render(request, 'index.html', {'form' : form, "today":today})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
    elif request.method == "GET":
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

'''
# Create your views here.
def signup_view(request):
    today = datetime.now()
    return render(request, 'index.html',{"today":today})
'''