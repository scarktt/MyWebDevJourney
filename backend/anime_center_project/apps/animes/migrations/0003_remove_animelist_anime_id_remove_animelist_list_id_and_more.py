# Generated by Django 4.1 on 2022-08-24 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
        ('animes', '0002_animelist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animelist',
            name='anime_id',
        ),
        migrations.RemoveField(
            model_name='animelist',
            name='list_id',
        ),
        migrations.RemoveField(
            model_name='useranime',
            name='anime_id',
        ),
        migrations.RemoveField(
            model_name='useranime',
            name='user_id',
        ),
        migrations.AddField(
            model_name='anime',
            name='genre',
            field=models.ManyToManyField(to='genres.genre'),
        ),
        migrations.DeleteModel(
            name='AnimeGenres',
        ),
        migrations.DeleteModel(
            name='AnimeList',
        ),
        migrations.DeleteModel(
            name='UserAnime',
        ),
    ]