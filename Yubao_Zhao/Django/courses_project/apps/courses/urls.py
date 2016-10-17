from django.conf.urls import url
from .views import *
# from . import views

urlpatterns = [
    url(r'^$', index),
    url(r'^courses/create$', create_course),
    url(r'^courses/(?P<course_id>\d+)/destroy$', destroy_course, name='destroy_course'),
    url(r'^comments/(?P<course_id>\d+)/show$', show_comment, name='show_comment'),
    url(r'^comments/(?P<course_id>\d+)/create$', create_comment, name='create_comment'),
    url(r'^comments/(?P<comment_id>\d+)/destroy$', destroy_comment, name='destroy_comment'),
]
