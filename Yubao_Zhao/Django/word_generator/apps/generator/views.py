from django.shortcuts import render, redirect
from random import sample
from string import ascii_uppercase, digits

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'word' not in request.session:
        request.session['word'] = ""
    return render(request, 'generator/index.html')

def generate(request):
    if request.method == 'POST':
        request.session['count'] += 1
        request.session['word'] = ''.join(sample(ascii_uppercase+digits, 14))
    return redirect('/')

def reset(request):
    del request.session['count']
    del request.session['word']
    return redirect('/')
