from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^initialize', views.init),
    url(r'^create$', views.create)     # This line has changed!
  ]
