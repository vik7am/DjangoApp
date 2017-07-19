# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def signup_view(request):
  today = datetime.now()
  return render(request, 'index.html',{"today":today})