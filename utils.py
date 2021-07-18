import json, ast

from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.gdal.error import GDALException
from swamps.models import BluemountainsThpssE448032756, SurveySite, SurveyData
from swamps.data import biocollect_response, macro_invertebrate_survey, surface_water_mineral_composition_survey,\
    vegetation_health_survey, water_table_and_water_physics_survey, wetland_sediment_survey

surveys = [
    macro_invertebrate_survey,
    surface_water_mineral_composition_survey,
    vegetation_health_survey,
    water_table_and_water_physics_survey,
    wetland_sediment_survey
]


def update_from_biocollect():
    # Create/update physical survey sites
    response = {}
    for survey in surveys:
        for site_data in survey['data']['searchBioCollectProject'][0].get('sites'):
            site_geojson = json.dumps(site_data.get('siteGeojson').get('geometry'))
            try:
                geometry = GEOSGeometry(site_geojson)
            except GDALException:
                # it appears the siteGeojson.geometry.coordinates[0] actually comes as a string, rather than a list in the raw data.
                site_data['siteGeojson']['geometry']['coordinates'] = [ast.literal_eval(site_data.get('siteGeojson').get('geometry').get('coordinates')[0])]
                site_geojson = json.dumps(site_data.get('siteGeojson').get('geometry'))
                geometry = GEOSGeometry(site_geojson)
            defaults = {
                'name': site_data.get('name'),
                'the_geom': geometry
            }
            survey_site, created = SurveySite.objects.update_or_create(
                site_id=site_data.get('siteId'),
                defaults=defaults,
            )

    return response
