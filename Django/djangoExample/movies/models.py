# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from enum import Enum

from django.db import models
import time


# Create your models here.

# class MyModel(models.Model):
#     created_at = models.DateTimeField('Created at', auto_now_add=True)
#
#     def __str__(self):
#         return self.name

class Genre(Enum):
    TERROR = 'TERROR'
    ACTION = 'ACTION'
    DRAMA = 'DRAMA'
    THRILLER = 'THRILLER'

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]



class Director(models.Model):
    name = models.CharField('Name', max_length=50)
    birht_date = models.DateField('Birth Date', blank=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    # GENRES = {
    #     (1, 'TERROR'),
    #     (2, 'ACTION'),
    #     (3, 'DRAMA'),
    #     (4, 'THRILLER'),
    # }
    #
    # GENRES = [
    #     'TERROR',
    #     'ACTION',
    #     'DRAMA',
    #     'THRILLER',
    # ]

    def uploadImageDirectory(self, filename):
        return 'moviePosters/%s_%s' % (time.time(), filename)

    title = models.CharField('Title', max_length=40, null=False, default='untitled')
    plot = models.CharField('Movie Plot', max_length=1000, null=False, default='No plot defined')
    units = models.DecimalField('Available Units', max_digits=4, decimal_places=0, default=1)
    # genre = models.CharField('Genre', choices=[(tag, tag.value) for tag in Genre], default=Genre.ACTION, max_length=20)
    genre = models.CharField('Genre', choices=Genre.choices(), default=Genre.ACTION, max_length=20)

    poster = models.ImageField('Poster', upload_to=uploadImageDirectory, null=True)

    director_id = models.ForeignKey(Director, on_delete=models.DO_NOTHING, related_name='movie')

    # Linea usada para que se vea el titulo desde el admin
    def __str__(self):
        return self.title
