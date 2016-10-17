from django.shortcuts import render, redirect
# from django.core.urlresolvers import reverse
from django.urls import reverse
from .models import *

def index(request):
    courses = Course.objects.all()
    context = {'courses' : courses}
    return render(request, 'courses/index.html', context)

def create_course(request):
    if request.method == 'POST':
        course = request.POST['course']
        desc = request.POST['description']
        if (course and not course.isspace()) and (desc and not desc.isspace()):
            c = Course.objects.create(name=course)
            Description.objects.create(content=desc, course=c)
    return redirect('/')

def destroy_course(request, course_id):
    course = Course.objects.get(id=course_id)
    # comments = Comment.objects.filter(course=course_id)  #course=course #course__id=course_id
    comments = course.comment_set.all()
    if request.method == 'GET':
        context = {'course' : course, 'comments' : comments}
        return render(request, 'courses/confirm.html', context)
    course.delete()
    return redirect('/')

def show_comment(request, course_id):
    course = Course.objects.get(id=course_id)
    comments = Comment.objects.filter(course__id=course_id)
    request.session['course_id'] = course_id
    context = {
        'course' : course,
        'comments' : comments
    }
    return render(request, 'courses/comment.html', context)

def create_comment(request, course_id):
    if request.method == 'POST':
        comment = request.POST['comment']
        if comment and not comment.isspace():
            course = Course.objects.get(id=course_id)
            Comment.objects.create(content=comment, course=course)
    # url = '/comments/{}/show'.format(course_id)
    return redirect(reverse('show_comment', kwargs={'course_id': course_id}))

def destroy_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    url = '/comments/{}/show'.format(request.session['course_id'])
    return redirect(url)
