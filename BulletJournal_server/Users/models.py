# Create your models here.
from django.db import models


class Role(models.Model):
    role_id = models.BigAutoField("Role id", db_column='BID', primary_key=True)
    role_name = models.CharField("Role Name", max_length=20)
    description = models.CharField("Role Description", max_length=200)

    def __str__(self):
        return f"{self.role_id, self.role_name, self.description}"


class User(models.Model):
    login = models.CharField("Login", max_length=20)
    email = models.EmailField("Email")
    password = models.CharField("Password", max_length=50)
    user_id = models.BigAutoField("User id", db_column='BID', primary_key=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_id, self.login, self.email}"
