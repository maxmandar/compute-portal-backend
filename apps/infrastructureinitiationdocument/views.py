
from rest_framework import generics
from .models import IidProject
from .serializers import IidProjectSerializer

from .models import IidRequestor
from .serializers import IidRequestorSerializer



class IidProjectListCreateView(generics.ListCreateAPIView):
    queryset = IidProject.objects.all()
    serializer_class = IidProjectSerializer

    def perform_create(self, serializer):
        iid_project = serializer.save()
        requestor = self.request.user
        IidRequestor.objects.create(iid_project=iid_project, requestor=requestor)



class IidProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IidProject.objects.all()
    serializer_class = IidProjectSerializer


class IidRequestorListCreate(generics.ListCreateAPIView):
    queryset = IidRequestor.objects.all()
    serializer_class = IidRequestorSerializer



class IidRequestorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = IidRequestor.objects.all()
    serializer_class = IidRequestorSerializer
