from django.conf.urls import url, include
from . import views

url(r'^$', views.login_page, name='index'),