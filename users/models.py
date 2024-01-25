from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='email', **NULLABLE)
    is_vendor = models.BooleanField(verbose_name='is vendor', default=False)
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
