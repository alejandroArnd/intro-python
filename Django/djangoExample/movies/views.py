# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import  HttpResponse

from django.shortcuts import render

# Create your views here.


def defaultView(request):
    context = {
        'sample': 'Hola'
    }

    return render(request, 'movies.html', context)
    #return HttpResponse("Welcome!")