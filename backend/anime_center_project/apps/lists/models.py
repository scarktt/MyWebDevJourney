from django.db import models

from .. animes.models import Anime


class List(models.Model):
    list_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_private = models.BooleanField(default=False)
    anime = models.ManyToManyField(Anime)


    def __str__(self):
        return self.name
