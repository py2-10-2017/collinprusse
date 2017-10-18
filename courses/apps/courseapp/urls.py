from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.index),
    url(r'^courses/add$', views.add),
    url(r'^courses/(?P<cid>\d+)/remove$', views.removePage),
    url(r'^courses/(?P<cid>\d+)/delete$', views.delete)     # This line has changed!
  ]
