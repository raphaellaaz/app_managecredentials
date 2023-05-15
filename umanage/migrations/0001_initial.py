# Generated by Django 4.2.1 on 2023-05-15 03:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='credentials_user',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('5a814874-5774-4c23-8b8d-44e4f15df910'), editable=False, primary_key=True, serialize=False)),
                ('tipo', models.CharField(default='No asignado', max_length=30, null=True)),
                ('name_credential', models.CharField(max_length=60)),
                ('pass_credential', models.CharField(max_length=100)),
                ('user_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credentials', to='login.ulogin')),
            ],
        ),
    ]
