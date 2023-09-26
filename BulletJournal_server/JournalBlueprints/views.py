from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters

from JournalBlueprints.models import Blueprint
from JournalBlueprints.serialiser import BlueprintSerialazers

class BulletBlueprintFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='iexact')
    max_count_of_markers = filters.NumberFilter()

    class Meta:
        models = Blueprint
        fields = ('name', 'creator', 'max_count_of_markers',)

class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class Blueprints(generics.ListAPIView):
    queryset = Blueprint.objects.all()
    serializer_class = BlueprintSerialazers
    pagination_class = Pagination

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BulletBlueprintFilter
    #filterset_fields = ('name', 'creator', 'max_count_of_markers',)

    '''def get_queryset(self):
        blueprint = Blueprint.objects.all()
        requests = self.request.query_params
        print(requests.get())
        blueprint.filter(requests)

        return blueprint'''

    '''def get(self, request):
        filters_query = BulletBlueprintFilters(request.GET, queryset=Blueprint.objects.all())
        context = {
            'form': filters_query.form,
            'blueprints': filters_query.qs
        }
        print(context)
        return Response(status=200)



    def post(self, request):
        #user = request.data.get("user")
        user_serializer = BlueprintSerialazers(data = request.data(), many=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(request, status= 200 + "User registrate")
        else:
            return Response(status = 400 + "Invalid data")


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

    def delete(self, request):
        id = request.GET.get("blueprint_id")

        try:
            obj = Blueprint.object.filter(blueprints_id = id)
        except:

            return Response(status=404)

        try:
            obj.destroy
            return Response(status=200)
        except:
            return Response(status=400)

'''