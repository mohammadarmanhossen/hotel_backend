from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.timezone import now

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
    district_names = models.ForeignKey(
        'District',
        on_delete=models.CASCADE,
        related_name='hotels',
        null=True,
        blank=True
    )
    image = models.ImageField(upload_to="hotels/images")
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available_room = models.PositiveIntegerField()

    def __str__(self):
        return self.hotel_name

    def district_name(self):
        return self.district_names.district_name if self.district_names else None


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
        return f'Review by {self.user.username}'  # Use hotel_name here


class Booked(models.Model):
    hotel_name = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room=models.PositiveIntegerField()
    in_date=models.DateField()
    out_date=models.DateField()
    payment=models.CharField(max_length=10, choices=PAYMENT) 

   
    