from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics

from .serializers import *


# views.py

class VmwareServerListView(generics.ListAPIView):
    serializer_class = VmwareServerListSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        bom_id = self.kwargs['bom_id']

        queryset = VmwareServer.objects.filter(project=project_id, bom=bom_id)
        return queryset

    

class VmwareServerCreateView(generics.CreateAPIView):
    queryset = VmwareServer.objects.all()
    serializer_class = VmwareServerCreateSerializer
  

class BigFixConfigCostsUpdateView(generics.UpdateAPIView):
    queryset = VmwareServer.objects.all()
    serializer_class = BigFixConfigCostsUpdateSerializer



# class ProjectBOMVmwareServerListView(generics.ListAPIView):
#     serializer_class = VmwareServerListSerializer

#     def get_queryset(self):
#         project_id = self.kwargs['project_id']
#         bom_id = self.kwargs['bom_id']

#         queryset = VmwareServer.objects.filter(project=project_id, bom=bom_id)
#         return queryset