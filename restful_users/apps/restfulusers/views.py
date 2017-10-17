from django.shortcuts import render
from .models import users
from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    context = {
        'users': users.objects.all()
    }
    return render(request, "restfulusers/index.html", context)
#a GET request to /users - calls the index method to display all the users. This will need a template.
def new(request):
    return render(request, "restfulusers/add.html")
#GET request to /users/new - calls the new method to display a form allowing users to create a new user. This will need a template.
def edit(request, uid):
    context = {
        'user': users.objects.get(id=uid)
    }
    return render(request, "restfulusers/edit.html", context)
#GET request /users/<id>/edit - calls the edit method to display a form allowing users to edit an existing user with the given id. This will need a template.
def show(request, uid):
    context = {
        'user': users.objects.get(id=uid)
    }
    return render(request, "restfulusers/show.html", context)
#GET /users/<id> - calls the show method to display the info for a particular user with given id. This will need a template.
def create(request):
    users.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
    )
    return redirect('/users')

#POST to /users/create - calls the create method to insert a new user record into our database. This POST should be sent from the form on the page /users/new. Have this redirect to /users/<id> once created.
def destroy(request, uid):
    b = users.objects.get(id=uid)
    b.delete()
    return redirect('/users')
#GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id. Have this redirect back to /users once deleted.
def update(request, uid):
    a = users.objects.get(id=uid)
    a.first_name = request.POST['first_name']
    a.last_name = request.POST['last_name']
    a.email = request.POST['email']
    a.save()
    return redirect('/users')
#POST /users/<id> - calls the update method to process the submitted form sent from /users/<id>/edit. Have this redirect to /users/<id> once updated.
