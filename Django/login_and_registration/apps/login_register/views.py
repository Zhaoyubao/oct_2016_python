from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import User

def index(request):
    if 'user' in request.session:
        messages.success(request, 'Welcome back!')
        return redirect('/success')
    return render(request, 'login_register/index.html')

def register(request):
    if request.method == 'POST':
        result = User.objects.validate_reg(request.POST)
        if result[0]:
            request.session['user'] = result[1]
            messages.success(request, 'Successfully registered!')
            return redirect(reverse('success'))
        print_messages(request, result[1])
    return redirect('/')

def login(request):
    if request.method == 'POST':
        result = User.objects.validate_log(request.POST)
        if result[0]:
            request.session['user'] = result[1]
            messages.success(request, 'Successfully logged in!')
            return redirect(reverse('success'))
        print_messages(request, result[1])
    return redirect('/')

def success(request):
    context = {'user' : request.session['user']}
    return render(request, 'login_register/success.html', context)

def logout(request):
    del request.session['user']
    return redirect('/')

def print_messages(request, error_list):
     for error, tag in error_list:
        messages.error(request, error, extra_tags=tag)
