from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    def create(self, request):
        user = User.objects.create_user(username=request['username'], email=request['email'],
            password = make_password(
                request['password']
            )
        )
        return user
        
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
