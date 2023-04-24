from django.contrib.auth.base_user import BaseUserManager

from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser


# Создаем класс менеджера пользователей



# Создаём класс User



# class UserManager(BaseUserManager):
#
#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self.create_user(email, password, **extra_fields)
#

class Competition(models.Model):
    title = models.CharField(max_length=255)
    season = models.ForeignKey("Season", on_delete=models.CASCADE, null=True)
    date = models.CharField(max_length=255)


class Season(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=255)


class Result(models.Model):
    sportsman = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255)
    gold_medals = models.IntegerField()
    silver_medals = models.IntegerField()
    bronze_medals = models.IntegerField()
    points = models.IntegerField()
    competition = models.ForeignKey("Competition", on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=255, blank=True)
