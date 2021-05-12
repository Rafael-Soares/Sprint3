from django.db import models


class auth_user(models.Model):
    username = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=25, blank=True)
