from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^home$', views.index),
    url(r'^add$', views.add),
    url(r'^create$', views.create),
    url(r'^(?P<book_id>\d+)$', views.show),
    url(r'^(?P<book_id>\d+)/create$', views.create_additional)
]
