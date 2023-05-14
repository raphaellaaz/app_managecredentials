from django.urls import path
from . import views

urlpatterns=[
    path('register/', views.register,name='register'),
    path('recovery/', views.recovery, name='recovery'),
    path('credentials/', views.credentials, name='credentials'),
]