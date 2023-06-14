from django.urls import path
from . import views

app_name='login'

urlpatterns=[
    path('', views.login_web, name='homelog'),
    path('reg/', views.register, name='register'),
    path('recover/', views.recover, name='recover'),
    path('logout/', views.userlogout, name='logout'),
]