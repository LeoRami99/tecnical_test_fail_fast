from rest_framework import viewsets
from user.models import Permission, Role, PermiUser, PermiRole, User, UserCompany
from .serializers import PermissionSerializer, RoleSerializer, PermiUserSerializer, PermiRoleSerializer, UserSerializer,UserCompanySerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class PermiUserViewSet(viewsets.ModelViewSet):
    queryset = PermiUser.objects.all()
    serializer_class = PermiUserSerializer

class PermiRoleViewSet(viewsets.ModelViewSet):
    queryset = PermiRole.objects.all()
    serializer_class = PermiRoleSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserCompanyViewSet(viewsets.ModelViewSet):
    queryset = UserCompany.objects.all()
    serializer_class = UserCompanySerializer
