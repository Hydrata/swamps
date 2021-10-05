from rest_framework import routers
from django.conf.urls import url, include
from swamps import api

router = routers.DefaultRouter()
router.register(r'survey-site', api.SurveySiteViewSet, 'survey-site')

app_name = 'swamps'

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/update-from-biocollect', api.update_from_biocollect_api, name='update_from_biocollect'),
    url(r'^api/update-from-airtables', api.update_from_airtables_api, name='update_from_airtables'),
]