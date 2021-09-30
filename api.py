from rest_framework.decorators import api_view
from rest_framework.response import Response

from swamps.utils import update_from_biocollect, update_from_airtables


@api_view()
def update_from_biocollect_api(request):
    response = update_from_biocollect()
    return Response(response)


@api_view()
def update_from_airtables_api(request):
    response = update_from_airtables()
    return Response(response)
