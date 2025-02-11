from django.db import models
from hotels.models import Booked
from django.contrib.auth.models import User
from hotels.models import Booked


class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booked = models.ManyToManyField(Booked)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    zip = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=7, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_amount = sum([booking.total_amount for booking in self.booked.all()])  
        super().save(*args, **kwargs)  #
    
    def __str__(self):  
        return self.name
    
