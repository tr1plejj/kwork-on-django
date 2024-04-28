
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from frlnc.settings import AUTH_USER_MODEL


class Order(models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=512)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order, related_name='orders')  # проекты, то есть задания, которые ты выкладываешь
    offers = models.ManyToManyField(Order, related_name='offers')  # задания, которые ты взял выполнять как исполнитель

    @receiver(post_save, sender=AUTH_USER_MODEL)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def __str__(self):
        return self.user.__str__()
