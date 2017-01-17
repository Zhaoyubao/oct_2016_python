from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^register$', register),
    url(r'^login$', login),
    url(r'^books$', home),
    url(r'^logout$', logout),
    url(r'^books/new$', new),
    url(r'^books/create$', create),
    url(r'^reviews/create/(?P<book_id>\d+)$', create_review),
    url(r'^reviews/delete/(?P<review_id>\d+)$', delete_review, name='delete_review'),
    url(r'^books/show/(?P<book_id>\d+)$', show_book, name='show_book'),
    url(r'^users/(?P<user_id>\d+)$', show_user, name='show_user'),
]
