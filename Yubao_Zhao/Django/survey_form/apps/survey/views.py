from django.shortcuts import render, redirect

def index(request):
    # del request.session['count']
    return render(request, 'survey/index.html')

def process(request):
    if request.method == 'POST':
        name = request.POST['username']
        if name and not name.isspace():
            request.session['username'] = name
            request.session['location'] = request.POST['location']
            request.session['language'] = request.POST['language']
            request.session['comment'] = request.POST['comment']
            return redirect('/result')
    return redirect('/')

def result(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    return render(request, 'survey/result.html')
