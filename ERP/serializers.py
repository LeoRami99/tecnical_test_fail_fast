from rest_framework import serializers
from .models import BranchOffice, CostCenter

class branch_officeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchOffice
        fields = '__all__'
class cost_centerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenter
        fields = '__all__'