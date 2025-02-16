from django.db import models
from hotels.models import Booked
from django.contrib.auth.models import User
from hotels.models import Booked
from hotels.models import Hotel


class Checkout(models.Model):
    booked = models.ForeignKey(Booked, on_delete=models.CASCADE, related_name="checkouts", default=1)  
    is_paid = models.BooleanField(default=False)



    