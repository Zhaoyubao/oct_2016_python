from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Product

def index(request):
    products = Product.objects.all()
    # print "Products:", products.values('id', 'name', 'description', 'price')
    return render(request, 'products/index.html', {'products' : products})

def show(request, id):
    p = Product.objects.get(id=id)
    return render(request, 'products/show.html', {'p' : p})

def new(request):
    return render(request, 'products/new.html')

def create(request):
    if request.method == 'POST':
        result = Product.objects.validate_new(request.POST)
        if result[0]:
            p = result[1]
            return redirect(reverse('show', kwargs={'id' : p.id}))
    for error in result[1]:
        messages.error(request, error)
    return redirect(reverse('new'))

def edit(request, id):
    p = Product.objects.get(id=id)
    return render(request, 'products/edit.html', {'p' : p})

def update(request, id):
    if request.method == 'POST':
        result = Product.objects.validate_update(request.POST, id)
        if result:
            return redirect(reverse('index'))
    return redirect(reverse('edit', kwargs={'id' : id}))

def destroy(request, id):
    Product.objects.get(id=id).delete()
    return redirect(reverse('index'))
