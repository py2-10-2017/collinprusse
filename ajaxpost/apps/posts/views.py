# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import posts
from django.shortcuts import render, HttpResponse
from django.core import serializers
import json

# Create your views here.
def index(request):
    return render(request, 'posts/index.html')

def init(request):
    return all_posts_json()

def all_posts_json():
    return HttpResponse(serializers.serialize("json", posts.objects.all()),
                        content_type='application/json')

def create(request):
    posts.objects.create(content=request.POST['content'])
    return all_posts_json()
