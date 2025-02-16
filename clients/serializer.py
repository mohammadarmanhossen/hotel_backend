from rest_framework import serializers
from django.contrib.auth.models import User
from .import models

from rest_framework import serializers




class ClientSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username') 
    first_name = serializers.ReadOnlyField(source='user.first_name')  
    last_name = serializers.ReadOnlyField(source='user.last_name')

    class Meta:
        model = models.Client
        fields = ['username', 'first_name', 'last_name', 'email', 'image']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = '__all__'

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Deposit
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        
        if password != password2:
            raise serializers.ValidationError({'error' : "Password Doesn't Mactched"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email Already exists"})
        account = User(username = username, email=email, first_name = first_name, last_name = last_name)
        print(account)
        account.set_password(password)
        account.is_active=False
        account.save()
        return account
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']







