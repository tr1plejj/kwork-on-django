from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    choices = (
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
    )
    first_name = models.CharField("first name", max_length=30)
    last_name = models.CharField("last name", max_length=30)
    email = models.EmailField("email")
    gender = models.CharField("gender", choices=choices, default='m')
    about = models.TextField("about", default='', blank=True)
    telegram = models.CharField("tg", max_length=64, default='', blank=True)
    vk = models.URLField("vk", default='', blank=True)

    REQUIRED_FIELDS = ["email", "first_name", "last_name", "gender"]
