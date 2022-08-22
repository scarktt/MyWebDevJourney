from django.db import models

from .. genres.models import Genre
from .. users.models import User

# watching, paused, finished
ANIME_STATE = (
    ('watching', 'Watching'),
    ('paused', 'Paused'),
    ('finished', 'Finished'),
)


class Broadcast(models.Model):
    broadcast_id = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=255)
    is_hidden = models.BooleanField(default=False)


class Season(models.Model):
    season_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255)
    season_year = models.DateTimeField()


class Anime(models.Model):
    anime_id = models.IntegerField(primary_key=True)
    images = models.JSONField("Images", default=dict)
    name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255)
    released = models.DateTimeField()
    episodes = models.IntegerField()
    category = models.CharField(max_length=255) 
    season_id = models.ForeignKey(Season, on_delete=models.SET_NULL, blank=True, null=True)
    broadcast_id = models.ForeignKey(Broadcast, on_delete=models.SET_NULL, blank=True, null=True)
    source = models.CharField(max_length=255)


class AnimeGenres(models.Model):
    anime_id = models.ForeignKey(Anime, on_delete=models.SET_NULL, blank=True, null=True)
    genre_id = models.ForeignKey(Genre, on_delete=models.SET_NULL, blank=True, null=True)


class UserAnime(models.Model):

    class States(models.TextChoices):
        WATCHING = 'watching', 'Watching'
        PAUSED = 'paused', 'Paused'
        FINISHED = 'finished', 'Finished'

    class Scores(models.IntegerChoices):
        one = 1, '1'
        two = 2, '2'
        three = 3, '3'
        four = 4, '4'
        five = 5, '5'

    useranime_id = models.IntegerField(primary_key=True)
    anime_id = models.ForeignKey(Anime, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=8, choices=States.choices)
    score = models.IntegerField(choices=Scores.choices)
