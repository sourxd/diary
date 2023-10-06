from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Notes(models.Model):
    name = models.ForeignKey(to=User, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text} || {self.name.username} ({self.name.first_name} {self.name.last_name})'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

