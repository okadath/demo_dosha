from django.db import models 
from django.utils import timezone
import datetime


class Product(models.Model):
    picture = models.FileField(upload_to='pics_product/', blank=True, null=True) 
    name =  models.CharField(max_length=149, blank=True, null=True)
    points = models.IntegerField(max_length=149, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Reward(models.Model):
    picture = models.FileField(upload_to='pics_reward/', blank=True, null=True) 
    name =  models.CharField(max_length=149, blank=True, null=True)
    value =  models.IntegerField(max_length=149, blank=True, null=True)
    # available = models.BooleanField(default=True)
    amount = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name


class Profile_Rewards(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, unique=True)
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    checker = models.ForeignKey(Profile, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return str(self.profile.user.username + '_' + self.reward.name)