# from django.apps import AppConfig


# class ExtendedUserConfig(AppConfig):
#     name = 'extended_user'
from django.apps import AppConfig


class UserAccountConfig(AppConfig):
    name ='extended_user'
    def ready(self):
        import extended_user.signals 