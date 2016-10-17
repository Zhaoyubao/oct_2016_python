from django.shortcuts import render, redirect
from .models import Email
from django.contrib import messages

def index(request):
    return render(request, 'validation/index.html')

def create(request):
    if request.method == 'POST':
        result = Email.emailMgr.validate(request.POST['email'])
        if result[0]:
            messages.success(request, 'The email address you entered ({}) is a VALID email address. Thank you!'.format(result[1].email))
            return redirect('/emails/show')
        messages.error(request, result[1][0], extra_tags='email')
    return redirect('/')

def show(request):
    emails = Email.emailMgr.all().order_by('-id')
    e = emails[0]
    context = {
        'emails' : emails,
        'e' : e
    }
    return render(request, 'validation/success.html', context)

def delete(request, email_id):
    e = Email.emailMgr.get(id=email_id)
    messages.success(request, "Email ({}) deleted successfully.".format(e.email))
    e.delete()
    return redirect('/emails/show')
