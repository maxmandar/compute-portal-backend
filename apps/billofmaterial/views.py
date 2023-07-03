# Create your views here.
from rest_framework import generics, permissions
from .models import BillOfMaterial
from .serializers import BillOfMaterialSerializer
from .permissions import IsInfraArchitectApprover, IsInfraArchitectVerifier



class BillOfMaterialListCreateView(generics.ListCreateAPIView):
    queryset = BillOfMaterial.objects.all()
    serializer_class = BillOfMaterialSerializer


class BillOfMaterialRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BillOfMaterial.objects.all()
    serializer_class = BillOfMaterialSerializer
    permission_classes = [permissions.IsAuthenticated, IsInfraArchitectVerifier]




