from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^emails/create$', create, name='create'),
    url(r'^emails/show$', show, name='show'),
    url(r'^emails/(?P<email_id>\d+)/delete$', delete, name='delete'),
]
