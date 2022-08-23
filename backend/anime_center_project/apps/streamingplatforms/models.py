from django.db import models

from .. animes.models import Anime


class StreamingPlatform(models.Model):
    streamingplatform_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    urls = models.CharField(max_length=255)


class AnimeStreamingPlatform(models.Model):
    anime_id = models.ForeignKey(Anime, on_delete=models.CASCADE)
    streamingplatform_id = models.ForeignKey(StreamingPlatform, on_delete=models.CASCADE)
    anime_url = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
