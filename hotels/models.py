from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.timezone import now
import requests

class District(models.Model):
    district_name= models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.district_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.district_name


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=255)
    address = models.TextField()
    district_names = models.ForeignKey('District', on_delete=models.CASCADE, related_name='hotels', null=True, blank=True)
    image_url = models.CharField(max_length=1024, blank=True)  
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available_room = models.PositiveIntegerField()

    def __str__(self):
        return self.hotel_name
    
    def district_name(self):
        return self.district_names.district_name if self.district_names else None

    def upload_image_to_imagebb(self, image_file):
        api_key = '91eb0ab92307af61f7bffe3b9d728952'
        url = 'https://api.imgbb.com/1/upload'
        payload = {
            'key': api_key,
            'image': image_file,
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            return response.json()['data']['url']
        return None

    def save(self, *args, **kwargs):
        if self.image_url:  
            self.image_url = self.upload_image_to_imagebb(self.image_url) 
        super().save(*args, **kwargs)





class Booked(models.Model):
    hotel_name = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.PositiveIntegerField()
    in_date = models.DateField()
    out_date = models.DateField()
    total_amount = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.hotel_name and self.room:
            self.total_amount = self.hotel_name.price_per_night * self.room
        super().save(*args, **kwargs) 

    def __str__(self):
        return f"{self.hotel_name}"



RATING_CHOICES = [
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
    ]
PAYMENT=[
    ('ssl','ssl'),
    ('Account','Account'),
]
class Review(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=10, choices=RATING_CHOICES) 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'Review by {self.user.username}' 
    
















    
    

