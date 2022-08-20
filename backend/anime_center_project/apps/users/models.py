from django.db import models

from datetime import date


class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)


class User(models.Model):
    user_id = models.CharField(max_length=25, primary_key=True)
    display_name = models.CharField(max_length=255, unique=True)
    birth_date = models.DateField(default=date.today, blank=True)
    email = models.EmailField(max_length=254)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    external_urls = models.JSONField("ExternalUrls", default=dict, blank=True)
    images = models.JSONField("Images", default=dict)


class Follower(models.Model):
    follower_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    begin_date = models.DateTimeField()
