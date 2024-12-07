
from django.contrib import admin
from .import models
# Register your models here.

admin.site.register(models.District)


# class HotelAdmin(admin.ModelAdmin):
#     list_display = ('name', 'district', 'price_per_night', 'available_room')
#     list_filter = ('district',)
#     search_fields = ('name', 'district__name')
#     ordering = ('name',)
#     fieldsets = (
#         ("Hotel Details", {
#             'fields': ('name', 'address', 'district', 'photo', 'description')
#         }),
#         ("Availability & Pricing", {
#             'fields': ('price_per_night', 'available_room')
#         }),
#     )

admin.site.register(models.Hotel)
admin.site.register(models.Review)