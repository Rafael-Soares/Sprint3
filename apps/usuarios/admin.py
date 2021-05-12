from apps.usuarios.models import auth_user
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(auth_user)