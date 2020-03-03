# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.test import TestCase

from .models import Director, Movie
# Create your tests here.


class BasicTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        director= Director.objects.create(name="Prueba", birht_date=datetime(2020, 1, 31))
        Movie.objects.create(title="prueba1",plot="Esto es una prueba01", units=2, points=1, voters=1,  director_id=director)
        Movie.objects.create(title="prueba2", plot="Esto es una prueba02", units=2, director_id=director)


    def test_true_is_true(self):
        self.assertEqual(True, True)

    def testCalculateRatingWhenPointsAndVotersAreNotZero(self):
        movie=Movie.objects.get(id=1)
        self.assertEqual(movie.calculateRating(),round(movie.points/movie.voters))

    def testCalculateRatingWhenPointsAndVotersAreZero(self):
        movie = Movie.objects.get(id=2)
        self.assertEqual(movie.calculateRating(),round(movie.points/movie.voters))


class ViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        director = Director.objects.create(name="Prueba", birht_date=datetime(2020, 1, 31))
        Movie.objects.create(title="prueba3", plot="Esto es una prueba03", poster="1582927429.0317125_índice.jpg" ,units=2, director_id=director)
        Movie.objects.create(title="prueba4", plot="Esto es una prueba04", poster="1582927429.0317125_índice.jpg", units=2, director_id=director)

    def testViewUrlExists(self):
        url="/movies/"
        resp=self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def testViewReturnAllMovies(self):
        url = "/movies/"
        resp = self.client.get(url)
        self.assertEqual(resp.context["movieList"].count(),2)