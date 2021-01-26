from .serializers import DebitSerializer
from rest_framework import viewsets, permissions
from .models import Debit

class DebitViewSet(viewsets.ModelViewSet):
    queryset = Debit.objects.all()
    serializer_class = DebitSerializer
    permission_classes = [permissions.IsAuthenticated]