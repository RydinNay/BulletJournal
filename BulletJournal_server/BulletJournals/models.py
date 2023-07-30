from django.db import models

from JournalBlueprints.models import Blueprint
from Users.models import User


class Variant(models.Model):

    name = models.CharField(max_length=40)
    variant_id = models.AutoField(db_column='BID', primary_key=True)

    def __str__(self):
        return f"{self.variant_id}"


class Journal(models.Model):

    name = models.CharField(max_length=30)
    journal_id = models.BigAutoField(db_column='BID', primary_key=True)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    blueprint = models.ForeignKey(Blueprint, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.journal_id}"