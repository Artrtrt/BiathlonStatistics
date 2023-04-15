from django.db import models


class PAPA(models.Model):
    titl = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
