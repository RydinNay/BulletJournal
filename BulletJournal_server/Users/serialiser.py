from rest_framework import serializers
from Users.models import User, Role


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ("role_name", "description")


class UserSerialazers(serializers.ModelSerializer):

    role = RoleSerializer()

    class Meta:
        model = User
        fields = ("login", "email", "user_id", "role")


class UserPostSerialiser():

    role = RoleSerializer()

    class Meta:
        model = User
        fields = ("login", "password", "email", "role")

