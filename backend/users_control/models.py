from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class MyUserManager(BaseUserManager):
    def _create_user(self, username, password, first_name, last_name, **extra_fields):

        if not username:
            raise ValueError("Вы не ввели Логин")
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, password, first_name, last_name):

        return self._create_user(username, password, first_name, last_name)

    def create_superuser(self,username, password, first_name, last_name):
        return self._create_user(username, password,first_name, last_name, is_staff=True, is_superuser=True)



class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'


    objects = MyUserManager()


    def __str__(self):
        return self.email
