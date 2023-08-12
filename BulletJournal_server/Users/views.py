from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from Users.models import User
from Users.serialiser import UserSerialazers


class Users(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerialazers(users, many=True)
        return Response(serializer.data)
