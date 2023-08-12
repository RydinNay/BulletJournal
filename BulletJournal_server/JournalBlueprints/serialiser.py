from rest_framework import serializers
from JournalBlueprints.models import Blueprint

class BlueprintSerialazers(serializers.ModelSerializer):

    class Meta:
        model = Blueprint
        fields = ("name", "blueprints_id", "creator", "max_count_of_markers")