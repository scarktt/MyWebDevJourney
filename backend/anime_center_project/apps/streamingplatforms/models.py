from django.db import models


class StreamingPlatform(models.Model):
    streamingplatform_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    urls = models.CharField(max_length=255)


    def __str__(self):
        return self.name


