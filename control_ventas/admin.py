from django.contrib import admin
from .models import *
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin as BaseAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib.sessions.models import Session


 
# admin.site.register(ControlDeploy)
 

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    search_fields = ('name' ,)
    # list_display = ('user', 'code',)
    # list_filter = ['code__region', ]
@admin.register(Reward)
class RewardAdmin(ImportExportModelAdmin):
    search_fields = ('name' ,)

@admin.register(Profile_Reward)
class Profile_RewardAdmin(ImportExportModelAdmin):
    search_fields = ('profile__user__username' ,"profile__id_user", "checker__user__username")

# @admin.register(User_Code)
# class UserCodeAdmin(ImportExportModelAdmin):
#     search_fields = ('code__code', 'user__username')
#     list_display = ('user', 'code',)
#     list_filter = ['code__region', ]


 
