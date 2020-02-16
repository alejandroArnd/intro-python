from django.conf.urls import url

from movies.views import defaultView

urlpatterns = [
    url(r'^$', defaultView, name='DeaultView')
    ]