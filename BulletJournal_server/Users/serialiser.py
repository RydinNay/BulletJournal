from rest_framework import serializers
from Users.models import User

class UserSerialazers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("login", "email", "password", "user_id", "role")