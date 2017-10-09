from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):

    return redirect('/')

def show(request, blog_id):
    response = "placeholder to display blog " + blog_id
    return HttpResponse(response)

def edit(request, blog_id):
    response = "placeholder to edit blog " + blog_id
    return HttpResponse(response)

def destroy(request, blog_id):
    return redirect('/')
