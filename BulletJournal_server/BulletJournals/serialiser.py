from rest_framework import serializers
from BulletJournals.models import Journal

class BulletJournalSerialazers(serializers.ModelSerializer):

    class Meta:
        model = Journal
        fields = ("name", "journal_id", "owner", "blueprint", "type", "termins", "count_of_markers")