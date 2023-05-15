from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid

class Ulogin(AbstractUser):
    #id=models.UUIDField(default=uuid.uuid4(), null=False, primary_key=True)
    email=models.EmailField(max_length=60, null=False, blank=False, unique=True)
    groups = models.ManyToManyField(Group, related_name='login_set')
    user_permissions = models.ManyToManyField(Permission, related_name='login_set')
    
    def __str__(self):
        return 'Login App'+ self.username
    

