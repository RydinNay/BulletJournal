import datetime

from django.db import models

from JournalBlueprints.models import Blueprint
from Users.models import User


class Journal(models.Model):

    name = models.CharField(max_length=30)
    journal_id = models.BigAutoField(db_column='BID', primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    blueprint = models.ForeignKey(Blueprint, on_delete=models.CASCADE, default=None)
    type = models.CharField(max_length=30, default='infinite')
    termins = models.DateField(default=datetime.date.today()+datetime.timedelta(days=3))
    count_of_markers = models.IntegerField(default=3)

    def __str__(self):
        return f"{self.journal_id}"