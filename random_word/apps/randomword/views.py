from __future__ import unicode_literals
import random
import string
from django.shortcuts import render, redirect

def random_word():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(14))

# Create your views here.
def index(request):
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 0

    return render(request, "randomword/index.html")

def generate(request):
    request.session['tries'] += 1
    request.session['word'] = random_word()
    return redirect('/')

def reset(request):
    del request.session['tries']
    del request.session['word']
    return redirect('/')
