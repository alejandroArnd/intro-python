from django.conf.urls import url
from django.urls import path


from .views import moviesList, showMovieData

urlpatterns = [
    url(r'^$', moviesList, name='Movies list'),
    path('<int:id>/', showMovieData, name="address_edit"),
]