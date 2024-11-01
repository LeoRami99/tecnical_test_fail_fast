from rest_framework import viewsets
from core.models import Company, EntityCatalog

from .serializers import CompanySerializer, EntityCatalogSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
class EntityCatalogViewSet(viewsets.ModelViewSet):
    queryset = EntityCatalog.objects.all()
    serializer_class = EntityCatalogSerializer