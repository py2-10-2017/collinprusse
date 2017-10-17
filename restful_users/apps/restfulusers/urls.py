from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.index),
    url(r'^users/new$', views.new),
    url(r'^users/(?P<uid>\d+)/edit$', views.edit),
    url(r'^users/(?P<uid>\d+)$', views.show),
    url(r'^users/create$', views.create),
    url(r'^users/(?P<uid>\d+)/destroy$', views.destroy),
    url(r'^users/(?P<uid>\d+)/update$', views.update)
  ]
