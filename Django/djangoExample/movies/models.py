# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MyModel(models.Model):
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    def __str__(self):
        return self.name

class Director(MyModel):
    name = models.CharField('Name', max_length=50, default='xd')
    birht_date = models.DateField("Birth Date", blank=True, null=True, default='2020/02/02')

class Movie(models.Model):
    GENRES = {
        (1, 'TERROR'),
        (2, 'ACCION')
    }

    title = models.CharField('Title', max_length=40, null=False, default='untitled')
    units = models.DecimalField('Available Units', max_digits=4, decimal_places=0, default=1)
    genre = models.PositiveSmallIntegerField('Genre', choices=GENRES, default=2)

    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING)

    # Linea usada para que se vea el titulo desde el admin
    def __str__(self):
        return self.title


