from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Viaje(models.Model):
    title = models.CharField(max_length = 30)
    description = models.CharField(max_length = 250)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(decimal_places = 2, max_digits = 6)
    image = models.CharField(max_length=5000)
    suscriptors = models.ManyToManyField(User)

    class Meta:
        ordering = ('title',)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    nation = models.TextField(max_length=30)
    trips = models.ManyToManyField(Viaje)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
