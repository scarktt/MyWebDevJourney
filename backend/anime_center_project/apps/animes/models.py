from django.db import models

from .. genres.models import Genre


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
    genre = models.ManyToManyField(Genre)


