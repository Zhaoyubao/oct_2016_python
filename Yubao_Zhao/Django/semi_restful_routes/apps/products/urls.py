from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^new$', new, name='new'),
    url(r'^(?P<id>\d+)$', show, name='show'),
    url(r'^edit/(?P<id>\d+)$', edit, name='edit'),
    url(r'^create$', create, name='create'),
    url(r'^update/(?P<id>\d+)$', update, name='update'),
    url(r'^destroy/(?P<id>\d+)$', destroy, name='destroy'),
]
