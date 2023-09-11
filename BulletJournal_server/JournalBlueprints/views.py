from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from JournalBlueprints.models import Blueprint
from JournalBlueprints.serialiser import BlueprintSerialazers


class BluePrints(APIView):

    def get(self, request):

        creator = request.GET.get("creator")

        try:
            blueprint = Blueprint.objects.filter(creator = creator)
            serializer = BlueprintSerialazers(blueprint, many=True)
            return Response(serializer.data, status=200)

        except:
            '''if creator == all'''
            blueprint = Blueprint.objects.all()
            serializer = BlueprintSerialazers(blueprint, many=True)
            return Response(serializer.data, status=201)


    def post(self, request):
        '''user = request.data.get("user")'''
        user_serializer = BlueprintSerialazers(data = request.data(), many=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"status": "200 User registrate"})
        else:
            return Response({"status": "Invalid data"})


    def put(self, request):
        id = request.GET.get("blueprints_id")

        try:
            obj = Blueprint.objects.filter(blueprints_id = id)
        except:
            message = {"error": "not found"}
            return Response(message, status=404)

        ser = BlueprintSerialazers(obj, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(status=200)
        return Response(status=400)