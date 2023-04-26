from django.db import models
import uuid

class login(models.Model):
    id=models.UUIDField(default=uuid.uuid4(), editable=False, primary_key=True, null=False)
    username=models.CharField(max_length=20, null=False)
    password=models.CharField(max_length=60, null=False)

    def __str__(self):
        return self.username
    
class user(models.Model):
    id=models.UUIDField(default=uuid.uuid4(), editable=False, primary_key=True, null=False)
    username=models.OneToOneField(login, on_delete=models.CASCADE, related_name='usuario')
    u_name=models.CharField(max_length=60, null=False, default='No asignado')
    u_lastname=models.CharField(max_length=60, null=False, default='No asignado')
    u_email=models.CharField(max_length=60, null=False, default='No asignado')
    u_borndate=models.DateField(null=False)
    u_phone=models.CharField(null=True, max_length=20)
    u_lastlogin=models.DateTimeField(null=False)
    
    def __str__(self):
        return self.u_name

class credentials_user(models.Model):
    id=models.UUIDField(default=uuid.uuid4(), editable=False, primary_key=True, null=False)
    tipo=models.CharField(default='No asignado', null=True, editable=True, max_length=30)
    name_credential=models.CharField(max_length=60, null=False)
    pass_credential=models.CharField(max_length=100, null=False)
    user_master=models.ForeignKey(user,on_delete=models.CASCADE, related_name='usercred')

    def __str__(self):
        return self.name_credential