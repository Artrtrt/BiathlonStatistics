from django.db import models


class Competition(models.Model):
    title = models.CharField(max_length=255)
    season = models.ForeignKey("Season", on_delete=models.CASCADE, null=True)
    date = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True)


class Season(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Result(models.Model):
    sportsman = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255)
    gold_medals = models.IntegerField()
    silver_medals = models.IntegerField()
    bronze_medals = models.IntegerField()
    points = models.IntegerField()
    competition = models.ForeignKey("Competition", on_delete=models.CASCADE, null=True)


