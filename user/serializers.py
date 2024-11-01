from rest_framework import serializers
from .models import Permission, Role, PermiUser, PermiRole, User, UserCompany

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Role
        fields = '__all__'

class PermiUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermiUser
        fields = '__all__'

class PermiRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermiRole
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class UserCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCompany
        fields = '__all__'
