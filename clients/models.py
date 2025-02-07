from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers



class Client(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="clients/image/")
    email=models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Contact(models.Model):
    subject=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return self.subject
class Deposit(models.Model):
    amount=models.PositiveIntegerField()
    
