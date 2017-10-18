from django.shortcuts import render, HttpResponse, redirect
from .models import courses
from django.contrib.messages import error
  # the index function is called when root is visited
def index(request):
    context = {
        'courses': courses.objects.all()
    }
    return render(request, "courseapp/index.html", context)

def add(request):
    errors = courses.objects.validate(request.POST)
    if errors:
        for err in errors:
            error(request, err)
    else:
        courses.objects.create(
            name=request.POST['name'],
            desc=request.POST['desc']
        )
    return redirect('/courses')

def removePage(request, cid):
    context = {
        'course': courses.objects.get(id=cid)
    }
    return render(request, "courseapp/delete.html", context)

def delete(request, cid):
    b = courses.objects.get(id=cid)
    b.delete()
    return redirect('/courses')
