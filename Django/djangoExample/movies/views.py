# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import  HttpResponse

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
    #return HttpResponse("Welcome!")


def showMovieData(request, id):
    context = {
        'movie': Movie.objects.get(id=id),
        'siteName': SITE_NAME
    }

    return render(request, 'movieInfo.html', context)