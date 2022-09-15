from django.db import models 
from django.utils import timezone
import datetime
from extended_user.models import Profile

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


class Profile_Reward(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name="reward_profile")
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    checker = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name="reward_checker")
    validity_expires = models.DateField( default=timezone.now() )

    def __str__(self):
        return str(self.profile.user.username + '_' + self.reward.name)

class Profile_Product(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name="product_profile")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    checker = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name="product_checker")
    validity_expires = models.DateField( default=timezone.now() )

    def __str__(self):
        return str(self.profile.user.username + '_' + self.reward.name)