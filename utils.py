import json
import ast
import requests

from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.gdal.error import GDALException
from django.conf import settings

from swamps.models import BluemountainsThpssE448032756, SurveySite
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
    headers={'Authorization': f'Bearer {settings.AIRTABLE_KEY}'}  # Read-only airtable key
    response = requests.get(
        "https://api.airtable.com/v0/appc1i4ybYpQqjCBp/survey_sites",
        headers=headers
    )
    sites_dict = response.json().get('records')
    site_activities = None
    for site in sites_dict:
        fields = site.get('fields')
        accessed_fields = list()
        if not site_activities:
            site_activities = dict()
        geometry = GEOSGeometry(
            f"POINT({fields.get('longitude')} {fields.get('latitude')})",
            srid=4326
        )
        try:
            swamp = BluemountainsThpssE448032756.objects.get(fid=fields.get('swamp_fid'))
        except BluemountainsThpssE448032756.DoesNotExist:
            swamp = None
        defaults = {
            'name': fields.get('name'),
            'swamp': swamp,
            'the_geom': geometry
        }
        for field in fields.items():
            print('field:', field)
            if type(field[1]) == list and field[0] not in accessed_fields:
                url = f"https://api.airtable.com/v0/appc1i4ybYpQqjCBp/{field[0]}/"
                response = requests.get(url, headers=headers)
                if response.status_code == 404:
                    print('not found: ', url)
                    continue
                for record in response.json().get('records'):
                    if site.get('id') in record.get('fields').get('location'):
                        if not site_activities.get(field[0]):
                            site_activities[field[0]] = list()
                        updated_activities = site_activities.get(field[0])
                        updated_activities.append(record)
                        site_activities[field[0]] = updated_activities
                accessed_fields.append(field[0])

        survey_site, created = SurveySite.objects.update_or_create(
            site_id=site.get('id'),
            defaults=defaults
        )
        survey_site.activities = site_activities
        survey_site.save()
        site_activities = None
