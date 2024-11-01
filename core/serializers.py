from rest_framework import serializers
from .models import Company, EntityCatalog

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EntityCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityCatalog
        fields = '__all__'
