# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render
from forms import SignUpForm

def signup_view(request):
    if request.method == "POST":
        print 'Sign up form submitted'
    elif request.method == 'GET':
        form = SignUpForm()
    today = datetime.now()
    return render(request, 'index.html', {'form' : form,"today":today})

'''
# Create your views here.
def signup_view(request):
    today = datetime.now()
    return render(request, 'index.html',{"today":today})
'''