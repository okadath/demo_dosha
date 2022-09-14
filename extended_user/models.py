from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.
class Profile(models.Model):
    # picture = models.FileField(upload_to='pics/', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    es_checador = models.BooleanField(default=False, verbose_name="Es Checador")
    id_user = models.CharField(max_length=149, blank=True, null=True)
    disponible_points = models.IntegerField( blank=True, null=True) 


    def __str__(self):
        return self.user.username