# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Pelicula
from .models import Director

# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Director)