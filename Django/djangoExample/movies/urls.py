from django.conf.urls import url
from django.urls import path

from .views import listaPeliculas, mostrarPelicula, alquilarPelicula, puntuarPelicula

urlpatterns = [
    url(r'^$', listaPeliculas, name='lista_peliculas'),
    path('<int:id>/', mostrarPelicula, name="ver_pelicula"),
    path('alquilar/', alquilarPelicula, name="alquilar_pelicula"),
    path('puntuar/<int:id>/', puntuarPelicula, name="puntuar_pelicula")
]
