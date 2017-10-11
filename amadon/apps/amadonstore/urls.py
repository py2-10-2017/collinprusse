from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^buy/(?P<item_id>\d+)', views.purchase),
    url(r'^checkout$', views.checkout)     # This line has changed!
  ]
