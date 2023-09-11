from django.contrib import admin
from django.urls import path, include
from BulletJournals.views import *

urlpatterns = [
    path('journals', Journals.as_view())
]
