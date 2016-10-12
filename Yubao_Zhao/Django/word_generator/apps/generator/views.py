from django.shortcuts import render, redirect
from random import sample
from string import ascii_uppercase, digits

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
        context = {'word' : ''}
    else:
        request.session['count'] += 1
        rand_word = ''.join(sample(ascii_uppercase+digits, 14))
        context = {'word' : rand_word}
    return render(request, 'generator/index.html', context)

def reset(request):
    del request.session['count']
    return redirect('/')
