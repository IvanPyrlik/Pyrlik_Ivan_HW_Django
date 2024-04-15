from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, max_length=300, verbose_name="Почта")

    avatar = models.ImageField(upload_to='media/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=15, verbose_name='Номер телефона', **NULLABLE)
    country = models.CharField(max_length=15, verbose_name='Страна', **NULLABLE)
    verification_code = models.CharField(max_length=9, verbose_name='Код верификации', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
