# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from enum import Enum

from django.core.validators import MinValueValidator, MaxValueValidator
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

    def calculateRating(self):
        result = 0

        if self.points != 0 and self.voters != 0:
            result = round(self.points / self.voters, 1)

        return result

    title = models.CharField('Title', max_length=40, null=False, default='untitled')
    plot = models.CharField('Movie Plot', max_length=1000, null=False, default='No plot defined')
    units = models.DecimalField('Available Units', max_digits=4, decimal_places=0, default=0,
                                validators=[MinValueValidator(0), MaxValueValidator(999)])
    genre = models.CharField('Genre', choices=Genre.choices(), default=Genre.ACTION, max_length=20)
    poster = models.ImageField('Poster', upload_to=uploadImageDirectory, null=True)

    points = models.IntegerField('Points', default=1, null=False, blank=False)
    voters = models.IntegerField('Voters', default=1, null=False, blank=False)

    director_id = models.ForeignKey(Director, on_delete=models.DO_NOTHING, related_name='movie')

    # Linea usada para que se vea el titulo desde el admin
    def __str__(self):
        return self.title
