from django.db import models

class User(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    display_name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=254)
    country = models.CharField(max_length=90, blank=True, null=True)
    external_urls = models.JSONField("ExternalUrls", default=dict, blank=True)
    followers = models.IntegerField()
    images = models.JSONField("Images", default=dict)


