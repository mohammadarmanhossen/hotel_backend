from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
# Create your models here.


class Client(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="clients/image/")
    email=models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

