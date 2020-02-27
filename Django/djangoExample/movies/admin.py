# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Movie
from .models import Director

# Register your models here.
admin.site.register(Movie)
admin.site.register(Director)