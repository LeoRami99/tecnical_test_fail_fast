from rest_framework import viewsets
from ERP.models import BranchOffice, CostCenter
from .serializers import branch_officeSerializer, cost_centerSerializer 


class BranchOfficeViewSet(viewsets.ModelViewSet):
    queryset = BranchOffice.objects.all()
    serializer_class = branch_officeSerializer
class CostCenterViewSet(viewsets.ModelViewSet):
    queryset = CostCenter.objects.all()
    serializer_class = cost_centerSerializer

    
