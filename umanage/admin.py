from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import login, user

admin.site.register(login)
admin.site.register(user)
