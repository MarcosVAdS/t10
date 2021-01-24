from rest_framework import serializers
from .models import Debit

class DebitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Debit
        fields =  ['requester', 'value', 'target', 'status', 'is_enable']