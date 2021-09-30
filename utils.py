import json
import ast
import requests

from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.gdal.error import GDALException

from swamps.models import BluemountainsThpssE448032756, SurveySite, SurveyData
from swamps.data import biocollect_response, macro_invertebrate_survey, surface_water_mineral_composition_survey,\
    vegetation_health_survey, water_table_and_water_physics_survey, wetland_sediment_survey


def update_from_biocollect():
    # Create/update physical survey sites
    response = {}
    surveys = [
        macro_invertebrate_survey,
        surface_water_mineral_composition_survey,
        vegetation_health_survey,
        water_table_and_water_physics_survey,
        wetland_sediment_survey
    ]
    activities = biocollect_response['data']['searchBioCollectProject'][0]['activities']

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
            if site_data['siteId'] == '747ac352-6ad7-438e-905a-e7a8bc2533dc':
                # Don't want to include the site boundary in any analysis
                geometry = None
            defaults = {
                'name': site_data.get('name'),
                'the_geom': geometry
            }
            survey_site, created = SurveySite.objects.update_or_create(
                site_id=site_data.get('siteId'),
                defaults=defaults,
            )

    for activity in activities:
        for item in activity['outputs'][0]['data']['dataList']:
            if item.get('key') == 'location':
                site = SurveySite.objects.get(site_id=item.get('value'))
                old_activities = site.activities
                item_exists = False
                for old_activity in old_activities:
                    if activity.get('activityId') == old_activity.get('activityId'):
                        item_exists = True
                        print(f'found activityId: {activity.get("activityId")} in site {site}')
                        continue
                if not item_exists:
                    new_activities = site.activities
                    new_activities.append(activity)
                    print('appending: ', site, activity)
                    site.activities = new_activities
                    site.save()
    return response


def update_from_airtables():
    #  Create/update the actual survey sites so they can be mapped
    response = requests.get(
        "https://api.airtable.com/v0/appc1i4ybYpQqjCBp/survey_locations?maxRecords=3&view=Grid%20view",
        headers={'Authorization': 'Bearer key1QftQfqYQw2LvF'}
    )
    sites_dict = response.json().get('records')
    for site in sites_dict:
        fields = site.get('fields')
        print('site: ', site)
        print('fields: ', fields)
        geometry = GEOSGeometry(
            f"POINT({fields.get('longitude')} {fields.get('latitude')})",
            srid=4326
        )
        defaults = {
            'name': fields.get('name'),
            'the_geom': geometry
        }
        survey_site, created = SurveySite.objects.update_or_create(
            site_id=site.get('id'),
            defaults=defaults,
        )
        if created:
            print('created: ', survey_site)
        else:
            print('updated:', survey_site)
