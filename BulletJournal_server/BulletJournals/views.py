from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from BulletJournals.models import Journal
from .serialiser import BulletJournalSerialazers


class Journals(APIView):

    def get(self, request):
        try:
            owner = request.GET.get("")
            journal = Journal.objects.filter(owner = owner)
            serializer = BulletJournalSerialazers(journal, many = True)
            return Response(serializer.data)

        except:

            journal = Journal.objects.all
            serializer = BulletJournalSerialazers(journal, many=True)
            return Response(serializer.data)


    def post(self, request):
        '''user = request.data.get("user")'''
        user_serializer = BulletJournalSerialazers(data = request.data(), many=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"status": "200 User registrate"})
        else:
            return Response({"status": "Invalid data"})