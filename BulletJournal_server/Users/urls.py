from django.urls import path, include
from Users.views import *

urlpatterns = [
    path('users/', Users.as_view())
]
