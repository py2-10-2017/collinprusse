from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit$', views.addWord),
    url(r'^clear$', views.clear)     # This line has changed!
  ]
