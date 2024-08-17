from rest_framework import serializers
from .models import Cars

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['brand', 'model', 'year', 'fuel_type', 'transmission_type', 'mileage', 'price']