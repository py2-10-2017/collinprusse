from django.shortcuts import render, redirect
from datetime import datetime
  # the index function is called when root is visited
def index(request):

    return render(request, "sessionwords/index.html")


def addWord(request):
    new_word = {}
    for key, value in request.POST.iteritems():
        if key != "csrfmiddlewaretoken" and key != "big":
            new_word[key] = value
        if key == "big":
            new_word['big'] = "big"
        else:
            new_word['big'] = ""
    new_word['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
    try:
        request.session['words']
    except KeyError:
        request.session['words'] = []

    temp_list = request.session['words']
    temp_list.append(new_word)
    request.session['words'] = temp_list
    for key, val in request.session.__dict__.iteritems():
        print key, val
    print "post created at", new_word
    return redirect('/')

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')
