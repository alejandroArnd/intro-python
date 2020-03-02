# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render

from .models import Movie

# Create your views here.
SITE_NAME = 'Movie Doctor'


def moviesList(request):
    context = {
        'movieList': Movie.objects.all(),
        'siteName': SITE_NAME
    }

    return render(request, 'movies.html', context)
    # return HttpResponse("Welcome!")


def showMovieData(request, id):
    context = {
        'movie': Movie.objects.get(id=id),
        'siteName': SITE_NAME
    }

    return render(request, 'movieInfo.html', context)


def rentMovie(request):
    response = {'status': 'ko'}

    id = request.POST.get("id")
    movie = Movie.objects.get(id=id)
    if movie.units > 0:
        movie.units -= 1
        movie.save()
        response = {'status': 'ok', 'units': movie.units}

    return JsonResponse(response)


def rateMovie(request, id):
    rating = request.GET.get('rating')

    movie = Movie.objects.get(id=id)
    movie.voters += 1
    movie.points += int(rating)
    movie.save()

    newAverage = movie.points / movie.voters
    return JsonResponse({'status': 'ok', 'newAverage': newAverage})
