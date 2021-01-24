from rest_framework import serializers
from .models import Partner

class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partner
        fields = ['name', 'cnpj', 'use_automatic_debit', 'is_enable']