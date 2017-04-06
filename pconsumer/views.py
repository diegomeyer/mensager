# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate

# Create your views here.
def chat(request):
    return render(request, 'pconsumer/chat.html')

def chat1(request):
    return render(request, 'pconsumer/chat1.html')


# Create your views here.
def home(request):
    user = authenticate(username='member', password='admin123')
    return render(request, 'pconsumer/home.html', {})