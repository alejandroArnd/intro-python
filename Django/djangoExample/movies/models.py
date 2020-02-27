# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# class MyModel(models.Model):
#     created_at = models.DateTimeField('Created at', auto_now_add=True)
#
#     def __str__(self):
#         return self.name

class Director(models.Model):
    name = models.CharField('Name', max_length=50)
    birht_date = models.DateField('Birth Date', blank=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    GENRES = {
        (1, 'TERROR'),
        (2, 'ACTION'),
        (3, 'DRAMA'),
        (4, 'THRILLER'),
    }

    def uploadImageDirectory(self, filename):
        return 'media/moviePosters/%s_%s' % (self.id, filename)

    title = models.CharField('Title', max_length=40, null=False, default='untitled')
    units = models.DecimalField('Available Units', max_digits=4, decimal_places=0, default=1)
    genre = models.PositiveSmallIntegerField('Genre', choices=GENRES, default=2)

    poster = models.ImageField('Poster', upload_to=uploadImageDirectory, null=True)

    director_id = models.ForeignKey(Director, on_delete=models.DO_NOTHING, related_name='movie')

    # Linea usada para que se vea el titulo desde el admin
    def __str__(self):
        return self.title