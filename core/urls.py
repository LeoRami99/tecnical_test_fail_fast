from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EntityCatalogViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'entity-catalogs', EntityCatalogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
