# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render

from .models import Pelicula

# Create your views here.
NOMBRE_WEB = 'Movie Doctor'


def listaPeliculas(request):
    context = {
        'listaPeliculas': Pelicula.objects.all(),
        'nombreWeb': NOMBRE_WEB
    }

    return render(request, 'movies.html', context)
    # return HttpResponse("Welcome!")


def mostrarPelicula(request, id):
    context = {
        'movie': Pelicula.objects.get(id=id),
        'siteName': NOMBRE_WEB
    }

    return render(request, 'movieInfo.html', context)


def alquilarPelicula(request):
    response = {'status': 'ko'}

    id = request.POST.get("id")
    movie = Pelicula.objects.get(id=id)
    if movie.units > 0:
        movie.units -= 1
        movie.save()
        response = {'status': 'ok', 'units': movie.units}

    return JsonResponse(response)


def puntuarPelicula(request, id):
    nota = request.GET.get('nota')

    pelicula = Pelicula.objects.get(id=id)
    pelicula.cantidad_votos += 1
    pelicula.puntos += int(nota)
    pelicula.save()

    nuevaMedia = pelicula.puntos / pelicula.cantidad_votos
    return JsonResponse({'status': 'ok', 'nuevaMedia': nuevaMedia})
