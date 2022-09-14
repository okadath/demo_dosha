from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib.sessions.models import Session


class UserResource(resources.ModelResource):
    class Meta:
        model = User

class UserAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = UserResource

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


 
# admin.site.register(Profile)
 

@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    search_fields = ('id_user',"user__username")