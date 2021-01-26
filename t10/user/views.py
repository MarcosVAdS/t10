from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from t10.user.serializers import UserSerializer
from django.contrib.auth import authenticate, login


class GetUsers(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
