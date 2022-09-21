from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from django.db.models.signals import post_save


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(_('Email Address'), unique=True)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    ratings = models.IntegerField( null=True, blank=True)
    reviews = models.CharField(max_length=280, null=True, blank=True)

    def __str__(self):
        return self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=CustomUser )




    