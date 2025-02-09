
from django.shortcuts import render
from rest_framework import viewsets
from .import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .import serializer


from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Booked, Hotel
from .serializer import BookedSerializer

class DistrictViewSet(viewsets.ModelViewSet):
    queryset=models.District.objects.all()
    serializer_class=serializer.DistrictSerializer
    lookup_field = 'slug'

class HotelViewSet(viewsets.ModelViewSet):
    queryset=models.Hotel.objects.all()
    serializer_class=serializer.HotelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['district_names'] 
    search_fields = ['hotel_name']  

class ReviewViewSet(viewsets.ModelViewSet):
    queryset=models.Review.objects.all()
    serializer_class=serializer.ReviewSerializer

# class BookedViewSet(viewsets.ModelViewSet):
#     queryset=models.Booked.objects.all()
#     serializer_class=serializer.BookedSerializer



class BookedViewSet(viewsets.ModelViewSet):
    queryset = Booked.objects.all()
    serializer_class = BookedSerializer



    