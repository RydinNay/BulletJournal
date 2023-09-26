from rest_framework import serializers
from JournalBlueprints.models import Blueprint
from Users.serialiser import UserSerialazers

class BlueprintSerialazers(serializers.ModelSerializer):

    creator = UserSerialazers()
    class Meta:
        model = Blueprint
        fields = ("name", "blueprints_id", "creator", "max_count_of_markers")#"__all__"
