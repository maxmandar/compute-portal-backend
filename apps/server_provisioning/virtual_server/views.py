from rest_framework import generics
from .models import VirtualServer
from .serializers import VirtualServerSerializer



class VirtualServerCreateView(generics.CreateAPIView):
    queryset = VirtualServer.objects.all()
    serializer_class = VirtualServerSerializer



class VirtualServerListView(generics.ListAPIView):
    serializer_class = VirtualServerSerializer
    
    def get_queryset(self):
        project_id = self.request.query_params.get('project_id')
        bom_id = self.request.query_params.get('bom_id')
        return VirtualServer.objects.filter(project_id=project_id, bom_id=bom_id)
    