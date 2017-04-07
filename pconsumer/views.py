# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import Room


# Create your views here.
def chat(request):
    room = Room.objects.get(label=0)
    messages = {}#room.messages.order_by('-timestamp')[:50]
    return render(request, 'pconsumer/chat.html', {'room': room.label, 'messages': messages})

def chat1(request):
    room = Room.objects.get(label=1)
    messages = {}#room.messages.order_by('-timestamp')[:50]
    return render(request, 'pconsumer/chat1.html', {'room': room.label, 'messages': messages})


# Create your views here.
def home(request):
    #user = authenticate(username='member', password='admin123')
    return render(request, 'pconsumer/home.html', {})