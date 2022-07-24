import imp
from pyexpat import model
from rest_framework import serializers
from powermeter.models import Medicion

class MedicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = ['sensor_data']
    