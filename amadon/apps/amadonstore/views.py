from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from inventory import items
  # the index function is called when root is visited
def index(request):
    if "last_transaction" in request.session.keys():
        del request.session['last_transaction']
    context = {
        "items": items
    }
    return render(request, "amadonstore/index.html", context)

def purchase(request, item_id):
    for item in items:
        if item['id'] == int(item_id):
            amount_charged = item['price'] * int(request.POST['quantity'])

    try:
        request.session['running_total']
    except KeyError:
        request.session['running_total'] = 0

    try:
        request.session['total_items']
    except KeyError:
        request.session['total_items'] = 0

    request.session['running_total'] += amount_charged
    request.session['total_items'] += int(request.POST['quantity'])
    request.session['last_transaction'] = amount_charged
    return redirect('/checkout')


def checkout(request):
    return render(request, "amadonstore/checkout.html")
