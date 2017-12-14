from django.conf.urls import url
from . import views  # "."(dot) means the same directory that this file currently in

urlpatterns = [
    url(r'^$', views.index, name='index'),  # the '^$' means home page
]