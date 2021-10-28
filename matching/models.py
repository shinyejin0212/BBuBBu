from django.db import models
from user.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib import auth

<<<<<<< HEAD
# class Match(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     followings = models.ManyToManyField("self", related_name="school_followers", symmetrical=False)

# @receiver(post_save, sender=User)
# def create_user_match(sender, instance, created, **kwargs):
#     if created:
#         Match.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_match(sender, instance, **kwargs):
#     instance.match.save()
=======
# Create your models here.
>>>>>>> d0ad08e104a459472ccb83f94a842f08bad92073
