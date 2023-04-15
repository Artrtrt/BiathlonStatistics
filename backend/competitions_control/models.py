from django.db import models


class Competition(models.Model):
    title = models.CharField(max_length=255)
    season = models.ForeignKey("Season", on_delete=models.CASCADE, null=True)
    date = models.DateField()


class Season(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return self.title


class Result(models.Model):
    sportsman = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    gold_medals = models.IntegerField()
    silver_medals = models.IntegerField()
    bronze_medals = models.IntegerField()
    points = models.IntegerField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)


class Category(models.Model):
    title = models.CharField(max_length=255)
    competition = models.ForeignKey("Competition", on_delete=models.CASCADE, null=True)
