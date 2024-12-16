from rest_framework import serializers
from .models import District
from .import models

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'district_name', 'slug']

class HotelSerializer(serializers.ModelSerializer):
    district_name=serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Hotel
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'

class BookedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booked
        fields = '__all__' 