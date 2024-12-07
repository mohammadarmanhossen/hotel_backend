
from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializer
# Create your views here.

class DistrictViewSet(viewsets.ModelViewSet):
    queryset=models.District.objects.all()
    serializer_class=serializer.DistrictSerializer
    lookup_field = 'slug'


class HotelViewSet(viewsets.ModelViewSet):
    queryset=models.Hotel.objects.all()
    serializer_class=serializer.HotelSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset=models.Review.objects.all()
    serializer_class=serializer.ReviewSerializer

class BookedViewSet(viewsets.ModelViewSet):
    queryset=models.Booked.objects.all()
    serializer_class=serializer.BookedSerializer
