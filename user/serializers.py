from rest_framework import serializers
from .models import Permission, Role, PermiUser, PermiRole

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
