from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from Users.models import User, Role
from Users.serialiser import UserSerialazers, RoleSerializer


class Users(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerialazers(users, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        '''user = request.data.get("user")'''
        user_serializer = UserSerialazers(data = request.data(), many=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"status": "200 User registrate"})
        else:
            return Response({"status": "Invalid data"})


class Roles(APIView):

    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return  Response({"data": serializer.data})
