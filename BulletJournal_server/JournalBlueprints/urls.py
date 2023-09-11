from django.urls import path, include
from JournalBlueprints.views import *

urlpatterns = [
    path('blueprints/', BluePrints.as_view()),
]
