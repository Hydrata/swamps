from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, permissions

from swamps.utils import update_from_biocollect, update_from_airtables
from swamps.models import SurveySite
from swamps.serializers import SurveySiteSerializer


@api_view()
def update_from_biocollect_api(request):
    response = update_from_biocollect()
    return Response(response)


@api_view()
def update_from_airtables_api(request):
    response = update_from_airtables()
    return Response(response)


class SurveySiteViewSet(viewsets.ModelViewSet):
    serializer_class = SurveySiteSerializer

    def get_queryset(self):
        queryset = SurveySite.objects.all()
        return queryset
