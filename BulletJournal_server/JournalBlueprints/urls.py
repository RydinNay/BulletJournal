from django.urls import path, include
from JournalBlueprints.views import Blueprints

urlpatterns = [
    path('blueprints/', Blueprints.as_view()),
]
