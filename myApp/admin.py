from django.contrib import admin
from .models import *

from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserModel(UserAdmin):
  display_list = ['username', 'user_type']
  
admin.site.register(CustomUser,UserModel)
