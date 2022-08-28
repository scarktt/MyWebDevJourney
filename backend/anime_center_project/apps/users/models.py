from django.db import models

from datetime import date

from .. animes.models import Anime
from .. lists.models import List


class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)


    def __str__(self):
        return self.name


class User(models.Model):
    user_id = models.CharField(max_length=25, primary_key=True)
    display_name = models.CharField(max_length=255, unique=True)
    birth_date = models.DateField(default=date.today, blank=True)
    email = models.EmailField(max_length=254)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    external_urls = models.JSONField("ExternalUrls", default=dict, blank=True)
    images = models.JSONField("Images", default=dict, blank=True)
    anime = models.ManyToManyField(Anime,
        through='UserAnime',
        related_name='user_id'
    )
    lists = models.ManyToManyField(List,
        through='UserList',
        related_name='user_id'
    )
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['user_id', 'created_at']


    def __str__(self):
        return self.display_name


class UserFollowing(models.Model):
    user_id = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    is_unfollowed = models.BooleanField(default=False)
    begin_date = models.DateTimeField()


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id','following_user_id'],  name="unique_followers")
        ]

        ordering = ["-begin_date"]


    def __str__(self):
        f"{self.user_id} follows {self.following_user_id}"


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

    anime_id = models.ForeignKey(Anime, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=8, choices=States.choices)
    score = models.IntegerField(choices=Scores.choices)


class UserList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    list_id = models.ForeignKey(List, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
