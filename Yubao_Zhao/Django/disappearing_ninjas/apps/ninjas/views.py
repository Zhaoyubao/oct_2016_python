from django.shortcuts import render

turtles = {"blue":"leonardo.jpg", "orange":"michelangelo.jpg", "red":"raphael.jpg", "purple":"donatello.jpg"}

def index(request):
    return render(request, 'ninjas/index.html')

def show_ninja(request, color):
    ninja = []
    if color:
        if color in turtles:
            ninja.append(turtles[color])
        else:
            ninja.append('notapril.jpg')
    else:
        for val in turtles.values():
            ninja.append(val)
    context = {'ninjas' : ninja}
    return render(request, 'ninjas/ninjas.html', context)
