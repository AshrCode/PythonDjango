from django.conf.urls import url
from . import views  # "."(dot) means the same directory that this file currently in

urlpatterns = [
    # /todolist/
    url(r'^$', views.index, name='index'),

    # /todolist/21/
    url(r'^(?P<list_id>[0-9]+)/$', views.detail, name='detail'),
]
