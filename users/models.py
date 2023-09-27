from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Notes(models.Model):
    name = models.ForeignKey(to=User, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'