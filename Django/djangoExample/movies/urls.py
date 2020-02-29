from django.conf.urls import url
from django.urls import path


from .views import moviesList, showMovieData, rentMovie

urlpatterns = [
    url(r'^$', moviesList, name='Movies list'),
    path('<int:id>/', showMovieData, name="address_edit"),
    path('rent/<int:id>/', rentMovie, name="rent a movie")
]