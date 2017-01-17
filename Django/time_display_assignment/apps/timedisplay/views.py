from django.shortcuts import render
import time

def index(request):
    date = time.strftime('%b %d, %Y')
    hour = time.strftime('%I:%M:%S %p')
    print date,hour
    context = {
            'date' : date,
            'time' : hour
    }
    return render(request, 'timedisplay/index.html', context)
