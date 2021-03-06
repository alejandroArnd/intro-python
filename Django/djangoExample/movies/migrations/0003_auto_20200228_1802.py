# Generated by Django 3.0.3 on 2020-02-28 18:02

from django.db import migrations, models
import movies.models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200227_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='plot',
            field=models.CharField(default='No plot defined', max_length=1000, verbose_name='Movie Plot'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(3, 'DRAMA'), (2, 'ACTION'), (1, 'TERROR'), (4, 'THRILLER')], default=2, verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(null=True, upload_to=movies.models.Movie.uploadImageDirectory, verbose_name='Poster'),
        ),
    ]
