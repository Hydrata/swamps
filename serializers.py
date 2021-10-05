from rest_framework import serializers

from swamps.models import SurveySite


class SurveySiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveySite
        fields = '__all__'
