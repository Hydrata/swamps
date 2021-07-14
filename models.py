from django.contrib.gis.db import models
from hydrata.models import GeospatialModel


class BluemountainsThpssE448032756(GeospatialModel):

    overall_status = models.CharField(max_length=256, blank=True, null=True, default='unknown')

    fid = models.AutoField(primary_key=True)
    the_geom = models.MultiPolygonField(srid=32756, blank=True, null=True)
    swamp_grou = models.CharField(db_column='SWAMP_GROU', max_length=254, blank=True, null=True)
    fid_1 = models.FloatField(db_column='FID_1', blank=True, null=True)
    swamp_gr_1 = models.CharField(db_column='SWAMP_GR_1', max_length=254, blank=True, null=True)
    cma = models.CharField(db_column='CMA', max_length=254, blank=True, null=True)
    catchment = models.CharField(db_column='CATCHMENT', max_length=254, blank=True, null=True)
    vegetation = models.CharField(db_column='VEGETATION', max_length=254, blank=True, null=True)
    veg_desc = models.CharField(db_column='VEG_DESC', max_length=254, blank=True, null=True)
    geology = models.CharField(db_column='GEOLOGY', max_length=254, blank=True, null=True)
    av_temp = models.FloatField(db_column='AV_TEMP', blank=True, null=True)
    av_rain = models.FloatField(db_column='AV_RAIN', blank=True, null=True)
    area_m2_1 = models.FloatField(db_column='AREA_M2_1', blank=True, null=True)
    elev_mean = models.FloatField(db_column='ELEV_MEAN', blank=True, null=True)
    swp_lgth_m = models.FloatField(db_column='SWP_LGTH_M', blank=True, null=True)
    er = models.FloatField(db_column='ER', blank=True, null=True)
    slope_min = models.FloatField(db_column='SLOPE_MIN', blank=True, null=True)
    slope_mean = models.FloatField(db_column='SLOPE_MEAN', blank=True, null=True)
    aspect = models.FloatField(db_column='ASPECT', blank=True, null=True)
    ca_m2 = models.FloatField(db_column='CA_M2', blank=True, null=True)
    ca_lgth_m = models.FloatField(db_column='CA_LGTH_M', blank=True, null=True)
    ca_er = models.FloatField(db_column='CA_ER', blank=True, null=True)
    d2c_m = models.FloatField(db_column='D2C_M', blank=True, null=True)
    d2c_ang = models.FloatField(db_column='D2C_ANG', blank=True, null=True)
    shape_leng = models.FloatField(db_column='Shape_Leng', blank=True, null=True)
    shape_area = models.FloatField(db_column='Shape_Area', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bluemountains_thpss_e_4480_32756'

