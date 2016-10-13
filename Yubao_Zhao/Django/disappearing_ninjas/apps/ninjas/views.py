from django.shortcuts import render

turtles = {"blue":"leonardo.jpg", "orange":"michelangelo.jpg", "red":"raphael.jpg", "purple":"donatello.jpg"}

def index(request):
    return render(request, 'ninjas/index.html')

def show_ninja(request, color):
    ninja = {}
    if color:
        if color in turtles:
            ninja[color] = turtles[color]
        else:
            ninja['megan'] = 'notapril.jpg'
        context = {'ninjas' : ninja}
    else:
        context = {'ninjas' : turtles}
    return render(request, 'ninjas/ninjas.html', context)
