# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Movie(models.Model):
    GENRES = {
        ('TERROR', 1),
        ('ACCION', 2)
    }

    title = models.CharField('Title', max_length=40)
    units = models.DecimalField('Available Units', max_digits=4, decimal_places=0, default=1)
    genre = models.PositiveSmallIntegerField('Genre', choices=GENRES, default=2)
