from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from extended_user.models import *
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from django.db import transaction
from django.utils import timezone
import datetime



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	"""
	una señal que crea un profile automaticamente al momento de registrar un nuevo usuario
	"""
	if created:
		Profile.objects.create(user=instance)
		# instance.username=instance.username.replace("@","_")
		instance.save()