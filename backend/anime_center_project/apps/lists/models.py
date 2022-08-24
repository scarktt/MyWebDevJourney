from django.db import models

from .. users.models import User


class List(models.Model):
    list_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_private = models.BooleanField(default=False)


class UserList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    list_id = models.ForeignKey(List, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

