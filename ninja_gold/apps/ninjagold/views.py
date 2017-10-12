from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random
  # the index function is called when root is visited
def index(request):
    return render(request, "ninjagold/index.html")

def process_money(request, place):
    try:
        request.session['gold']
    except:
        request.session['gold'] = 0

    try:
        request.session['log']
    except:
        request.session['log'] = []

    time = datetime.now().strftime("%Y/%m/%d %-I:%M%p")

    if place == "farm":
        gold = random.randrange(10,20)
        log = "Earned " + str(gold) + " gold from the farm! " + time
    elif place == "cave":
        gold = random.randrange(5,10)
        log = "Earned " + str(gold) + " gold from the cave! " + time
    elif place == "house":
        gold = random.randrange(2,5)
        log = "Earned " + str(gold) + " gold from the house! " + time
    elif place == "casino":
        gold = random.randrange(-50,50)
        if gold > 0:
            log = "Earned " + str(gold) + " gold from the casino! " + time
        else:
            log = "You lost " + str(gold) + " gold from the casino. Oh no! " + time

    try:
        running_log = request.session['log']
    except:
        running_log = []
    request.session['gold'] += gold

    running_log.append(log)
    request.session['log'] = running_log


    return redirect('/')

def clear(request):
    del request.session['gold']
    del request.session['log']
    return redirect('/')
