from django.db import models

from .. genres.models import Genre
from .. streamingplatforms.models import StreamingPlatform


class Broadcast(models.Model):
    broadcast_id = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=255)
    is_hidden = models.BooleanField(default=False)


    def __str__(self):
        return self.state


class Season(models.Model):
    season_id = models.IntegerField(primary_key=True)
    season = models.CharField(max_length=50)
    season_year = models.DateTimeField()


    def __str__(self):
        return self.season


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
    streaming_platform = models.ManyToManyField(StreamingPlatform,
        through='AnimeStreamingPlatform',
        related_name='anime_id'
    )


    class Meta:
        verbose_name = 'Anime'
        verbose_name_plural = 'Animes'
        ordering = ['name']


    def __str__(self):
        return self.name


class AnimeStreamingPlatform(models.Model):
    anime_id = models.ForeignKey(Anime, on_delete=models.CASCADE)
    streamingplatform_id = models.ForeignKey(StreamingPlatform, on_delete=models.CASCADE)
    anime_url = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
