from django.db import models


class Message(models.Model):
    message = models.CharField()
    login = models.CharField(max_length=255)

