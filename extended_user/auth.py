from extended_user.models import Profile 
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
# requires to define two functions authenticate and get_user
from django.contrib.auth.models import User

class EmailPasswordlessAuth(ModelBackend):  

    def authenticate(email=None):
        try:
            Prof = Profile.objects.get(user=User.objects.get(email=email).id)
            # print("el del auth es"+str(Prof))
            return Prof.user
        except Profile.DoesNotExist:
            return None

        return None

class IDPasswordlessAuth(ModelBackend):  

    def authenticate(id_user=None):
        try:
            Prof = Profile.objects.get(id_user=id_user)
            # print("el del auth es"+str(Prof))
            return Prof.user
        except Profile.DoesNotExist:
            return None

        return None

class UsernamePasswordlessAuth(ModelBackend):  

    def authenticate(username=None):
        try:
            Prof = Profile.objects.get(user=User.objects.get(username=username).id )
            # print("el del auth es"+str(Prof))
            return Prof.user
        except Profile.DoesNotExist:
            return None

        return None