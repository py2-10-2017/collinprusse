from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit$', views.submit),
    url(r'^result$', views.display_result)
  ]
