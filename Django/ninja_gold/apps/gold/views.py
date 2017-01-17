from django.shortcuts import render, redirect
from random import randint
import time

def index(request):
    try:
        request.session['gold']
        request.session['action']
    except:
        request.session['gold'] = 0
        request.session['action'] = []
    return render(request, 'gold/index.html')

def process(request, place):
    data = {'farm':randint(10,20), 'cave':randint(5,10),'house':randint(2,5), 'casino':randint(-50,50)}
    gold = data[place]
    now = time.strftime('%Y/%m/%d %I:%M:%S %p')
    if gold > 0:
        act = "green", "Earned {} golds from the {}! ({})".format(gold, place, now)
    elif gold < 0:
        act = "red", "Entered a casino and lost {} golds... Ouch.. ({})".format(-gold, now)
    else:
        act = "null", "Entered a casino and got nothing... ({})".format(now)
    request.session['gold'] += gold
    request.session['action'].append(act)
    return redirect('/')

def reset(request):
    del request.session['gold']
    del request.session['action']
    return redirect('/')
