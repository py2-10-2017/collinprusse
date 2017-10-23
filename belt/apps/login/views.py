# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import users
from ..reviews.models import books
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def register(request):
    result = users.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    return redirect('/home')

def login(request):
    result = users.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect ('/home')

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'user': users.objects.get(id=request.session['user_id'])
    }
    return render(request, 'login/success.html', context)

def show(request, user_id):
    user = users.objects.get(id=user_id)
    unique_ids = user.reviews_left.all().values("book").distinct()
    unique_books = []
    for book in unique_ids:
        unique_books.append(books.objects.get(id=book['book']))
    context = {
        'user': user,
        'unique_book_reviews': unique_books
    }
    return render(request, 'login/user.html', context)
