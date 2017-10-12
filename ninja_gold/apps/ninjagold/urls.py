from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^clear$', views.clear),
    url(r'^process_money/(?P<place>\w+)', views.process_money)     # This line has changed!
  ]
