
from django.contrib import admin
from .import models
# Register your models here.

admin.site.register(models.District)
admin.site.register(models.Hotel)
admin.site.register(models.Review)
admin.site.register(models.Booked)