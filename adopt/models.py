from django.db import models
from user.models import User
# Create your models here.
from django.dispatch import receiver
from django.db.models.signals import post_save


class Adopt(models.Model):
    application= models.BooleanField(default=False)
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    adopting=models.ManyToManyField("self",related_name="adopted",symmetrical=False)

@receiver(post_save, sender=User)
def create_user_adopt(sender, instance, created, **kwargs):
    if created:
        Adopt.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_adopt(sender,instance, **kwargs):
    instance.adopt.save()
    

