from django.urls import path
from . import views

urlpatterns=[
    path('', views.credentials, name='credentials'),
]