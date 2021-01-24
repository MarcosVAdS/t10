from .serializers import DebitSerializer
from rest_framework import viewsets, permissions
from .models import Debit

# Create your views here.
class DebitViewSet(viewsets.ModelViewSet):
    queryset = Debit.objects.all()
    serializer_class = DebitSerializer
    permission_classes = [permissions.IsAuthenticated]