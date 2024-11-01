from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PermissionViewSet, RoleViewSet, PermiUserViewSet, PermiRoleViewSet, UserViewSet, UserCompanyViewSet

router = DefaultRouter()
router.register(r'permissions', PermissionViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'permi-users', PermiUserViewSet)
router.register(r'permi-roles', PermiRoleViewSet)
router.register(r'users', UserViewSet)
router.register(r'user-companies', UserCompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
