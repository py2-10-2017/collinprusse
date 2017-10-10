from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):

    return render(request, "survey/index.html")

def display_result(request):
    return render(request, "survey/results.html")


def submit(request):
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 0
	#if request.method == "POST":
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['dojolocation']
    request.session['language'] = request.POST['favoritelanguage']
    request.session['desc'] = request.POST['description']
    request.session['tries'] += 1
    return redirect("/result")
	#else:
		#return redirect("/")
