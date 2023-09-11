from django.contrib import admin
from django.urls import path, include
from .views import Users, Roles

urlpatterns = [
    path('users/', Users.as_view()),
    path('roles/', Roles.as_view()),
]
