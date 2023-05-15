from django.urls import path
from . import views

urlpatterns=[
    path('', views.login_web, name='login'),
    path('reg/', views.register, name='register'),
    path('recover/', views.recover, name='recover')
]