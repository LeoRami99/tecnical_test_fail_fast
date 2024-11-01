from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BranchOfficeViewSet, CostCenterViewSet

router = DefaultRouter()
router.register(r'branch_offices', BranchOfficeViewSet)
router.register(r'cost_centers', CostCenterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
