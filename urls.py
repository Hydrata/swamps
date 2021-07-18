from django.conf.urls import url
from swamps import api
app_name = 'swamps'

urlpatterns = [
    url(r'^api/update-from-biocollect', api.update_from_biocollect_api, name='update_from_biocollect'),
]