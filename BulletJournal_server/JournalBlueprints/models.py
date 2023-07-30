from django.db import models
from Users.models import User


class Blueprint(models.Model):

    name = models.CharField("Blueprint name", max_length=30)
    blueprints_id = models.BigAutoField("Blueprint id", db_column='BID', primary_key=True)
    creator = models.ForeignKey(User, verbose_name="user_id", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.name, self.blueprints_id}"
# Create your models here.
