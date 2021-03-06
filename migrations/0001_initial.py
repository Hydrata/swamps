# Generated by Django 2.2.20 on 2021-07-14 07:43

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BluemountainsThpssE448032756',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('the_geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=32756)),
                ('swamp_grou', models.CharField(blank=True, db_column='SWAMP_GROU', max_length=254, null=True)),
                ('fid_1', models.FloatField(blank=True, db_column='FID_1', null=True)),
                ('swamp_gr_1', models.CharField(blank=True, db_column='SWAMP_GR_1', max_length=254, null=True)),
                ('cma', models.CharField(blank=True, db_column='CMA', max_length=254, null=True)),
                ('catchment', models.CharField(blank=True, db_column='CATCHMENT', max_length=254, null=True)),
                ('vegetation', models.CharField(blank=True, db_column='VEGETATION', max_length=254, null=True)),
                ('veg_desc', models.CharField(blank=True, db_column='VEG_DESC', max_length=254, null=True)),
                ('geology', models.CharField(blank=True, db_column='GEOLOGY', max_length=254, null=True)),
                ('av_temp', models.FloatField(blank=True, db_column='AV_TEMP', null=True)),
                ('av_rain', models.FloatField(blank=True, db_column='AV_RAIN', null=True)),
                ('area_m2_1', models.FloatField(blank=True, db_column='AREA_M2_1', null=True)),
                ('elev_mean', models.FloatField(blank=True, db_column='ELEV_MEAN', null=True)),
                ('swp_lgth_m', models.FloatField(blank=True, db_column='SWP_LGTH_M', null=True)),
                ('er', models.FloatField(blank=True, db_column='ER', null=True)),
                ('slope_min', models.FloatField(blank=True, db_column='SLOPE_MIN', null=True)),
                ('slope_mean', models.FloatField(blank=True, db_column='SLOPE_MEAN', null=True)),
                ('aspect', models.FloatField(blank=True, db_column='ASPECT', null=True)),
                ('ca_m2', models.FloatField(blank=True, db_column='CA_M2', null=True)),
                ('ca_lgth_m', models.FloatField(blank=True, db_column='CA_LGTH_M', null=True)),
                ('ca_er', models.FloatField(blank=True, db_column='CA_ER', null=True)),
                ('d2c_m', models.FloatField(blank=True, db_column='D2C_M', null=True)),
                ('d2c_ang', models.FloatField(blank=True, db_column='D2C_ANG', null=True)),
                ('shape_leng', models.FloatField(blank=True, db_column='Shape_Leng', null=True)),
                ('shape_area', models.FloatField(blank=True, db_column='Shape_Area', null=True)),
            ],
            options={
                'db_table': 'bluemountains_thpss_e_4480_32756',
                'managed': True,
            },
        ),
    ]
