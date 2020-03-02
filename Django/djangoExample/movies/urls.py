from django.conf.urls import url
from django.urls import path

from .views import moviesList, showMovieData, rentMovie, rateMovie

urlpatterns = [
    url(r'^$', moviesList, name='movies_list'),
    path('<int:id>/', showMovieData, name="address_edit"),
    path('rent/', rentMovie, name="rent_movie"),
    path('rate/<int:id>/', rateMovie, name="rate_movie")
]
