from rest_framework import serializers
from BulletJournals.models import Journal

from JournalBlueprints.serialiser import BlueprintSerialazers
from Users.serialiser import UserSerialazers
class BulletJournalSerialazers(serializers.ModelSerializer):

    owner = UserSerialazers()
    blueprint = BlueprintSerialazers()

    class Meta:
        model = Journal
        fields = ("name", "journal_id", "owner", "blueprint", "type", "termins", "count_of_markers")
