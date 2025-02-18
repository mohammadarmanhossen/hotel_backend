from rest_framework import serializers
from .models import District
from .import models

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'district_name', 'slug']


class HotelSerializer(serializers.ModelSerializer):
    district_name = serializers.CharField(source='district_names.district_name', read_only=True)

    class Meta:
        model = models.Hotel
        fields = [
            'id', 
            'hotel_name', 
            'address', 
            'district_name',  
            'image_url', 
            'description', 
            'price_per_night', 
            'available_room'
        ]

class BookedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booked
        fields = '__all__' 


class ReviewSerializer(serializers.ModelSerializer): 

    class Meta:
        model = models.Review
        fields = ['id', 'rating','created', 'body']


