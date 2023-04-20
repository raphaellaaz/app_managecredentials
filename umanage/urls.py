from django.urls import path
from . import views

urlpatterns=[
    path('', views.login_web, name='login'),
    path('prof/', views.profile_set, name='profile'),
    path('register/', views.register,name='register'),
    path('recovery/', views.recovery, name='recovery'),
]