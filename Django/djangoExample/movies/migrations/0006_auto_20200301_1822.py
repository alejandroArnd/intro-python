# Generated by Django 3.0.3 on 2020-03-01 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20200301_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='points',
            field=models.IntegerField(default=1, verbose_name='Points'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='voters',
            field=models.IntegerField(default=1, verbose_name='Voters'),
        ),
    ]
