from .views import *
from django.urls import path

urlpatterns = [
    path("register/", register, name='register'),
    path("login/", log_in, name='login'),
    path("change_password/", change_password, name='change_password'),
]
