from django.conf.urls import url
from . import views

#enrutadores

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$',)
]
