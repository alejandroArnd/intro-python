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

class Genero(Enum):
    TERROR = 'TERROR'
    ACCION = 'ACCION'
    DRAMA = 'DRAMA'
    THRILLER = 'THRILLER'

    @classmethod
    def elecciones(cls):
        return [(eleccion.name, eleccion.value) for eleccion in cls]


class Director(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', blank=True)

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
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

    def subirImagenAlDirectorio(self, nombreArchivo):
        return 'moviePosters/%s_%s' % (time.time(), nombreArchivo)

    def calcularNota(self):
        resultado = 0

        if self.puntos != 0 and self.cantidad_votos != 0:
            resultado = round(self.puntos / self.cantidad_votos, 1)

        return resultado

    titulo = models.CharField('Titulo', max_length=40, null=False, default='sin titulo')
    trama = models.CharField('Trama de la pelicula', max_length=1000, null=False, default='No hay trama definida')
    unidades = models.DecimalField('Unidades disponibles', max_digits=4, decimal_places=0, default=0,
                                   validators=[MinValueValidator(0), MaxValueValidator(999)])
    genero = models.CharField('Genero', choices=Genero.choices(), default=Genero.ACTION, max_length=20)
    poster = models.ImageField('Poster', upload_to=subirImagenAlDirectorio, null=True)

    puntos = models.IntegerField('Puntos', default=1, null=False, blank=False)
    cantidad_votos = models.IntegerField('Cantidad de votos', default=1, null=False, blank=False)

    director_id = models.ForeignKey(Director, on_delete=models.DO_NOTHING, related_name='pelicula')

    # Linea usada para que se vea el titulo desde el admin
    def __str__(self):
        return self.titulo
