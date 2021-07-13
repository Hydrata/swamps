from django.contrib.gis.db import models

# Create your models here.


class BluemountainsThpssE4480(models.Model):
    fid = models.AutoField(primary_key=True)
    the_geom = models.MultiPolygonField(srid=4283, blank=True, null=True)
    swamp_grou = models.CharField(db_column='SWAMP_GROU', max_length=254, blank=True, null=True)  # Field name made lowercase.
    fid_1 = models.FloatField(db_column='FID_1', blank=True, null=True)  # Field name made lowercase.
    swamp_gr_1 = models.CharField(db_column='SWAMP_GR_1', max_length=254, blank=True, null=True)  # Field name made lowercase.
    cma = models.CharField(db_column='CMA', max_length=254, blank=True, null=True)  # Field name made lowercase.
    catchment = models.CharField(db_column='CATCHMENT', max_length=254, blank=True, null=True)  # Field name made lowercase.
    vegetation = models.CharField(db_column='VEGETATION', max_length=254, blank=True, null=True)  # Field name made lowercase.
    veg_desc = models.CharField(db_column='VEG_DESC', max_length=254, blank=True, null=True)  # Field name made lowercase.
    geology = models.CharField(db_column='GEOLOGY', max_length=254, blank=True, null=True)  # Field name made lowercase.
    av_temp = models.FloatField(db_column='AV_TEMP', blank=True, null=True)  # Field name made lowercase.
    av_rain = models.FloatField(db_column='AV_RAIN', blank=True, null=True)  # Field name made lowercase.
    area_m2_1 = models.FloatField(db_column='AREA_M2_1', blank=True, null=True)  # Field name made lowercase.
    elev_mean = models.FloatField(db_column='ELEV_MEAN', blank=True, null=True)  # Field name made lowercase.
    swp_lgth_m = models.FloatField(db_column='SWP_LGTH_M', blank=True, null=True)  # Field name made lowercase.
    er = models.FloatField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    slope_min = models.FloatField(db_column='SLOPE_MIN', blank=True, null=True)  # Field name made lowercase.
    slope_mean = models.FloatField(db_column='SLOPE_MEAN', blank=True, null=True)  # Field name made lowercase.
    aspect = models.FloatField(db_column='ASPECT', blank=True, null=True)  # Field name made lowercase.
    ca_m2 = models.FloatField(db_column='CA_M2', blank=True, null=True)  # Field name made lowercase.
    ca_lgth_m = models.FloatField(db_column='CA_LGTH_M', blank=True, null=True)  # Field name made lowercase.
    ca_er = models.FloatField(db_column='CA_ER', blank=True, null=True)  # Field name made lowercase.
    d2c_m = models.FloatField(db_column='D2C_M', blank=True, null=True)  # Field name made lowercase.
    d2c_ang = models.FloatField(db_column='D2C_ANG', blank=True, null=True)  # Field name made lowercase.
    shape_leng = models.FloatField(db_column='Shape_Leng', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='Shape_Area', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bluemountains_thpss_e_4480'
