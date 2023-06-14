from django.db import models
#from login.models import Ulogin
import uuid

class credentials_user(models.Model):
    id=models.UUIDField(default=uuid.uuid4(), editable=False, primary_key=True, null=False)
    tipo=models.CharField(default='No asignado', null=True, editable=True, max_length=30)
    name_credential=models.CharField(max_length=60, null=False)
    pass_credential=models.CharField(max_length=100, null=False)
    #user_master=models.ForeignKey(Ulogin,on_delete=models.CASCADE, related_name='credentials')

    def __str__(self):
        return self.name_credential
