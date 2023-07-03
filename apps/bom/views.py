from rest_framework import generics

from .models import *
from .serializers import *


class EnvironmentListCreateView(generics.ListCreateAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer

class LayerListCreateView(generics.ListCreateAPIView):
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer
    

class OpenSystemsIntelVMWareSoftwareLicenseListCreateView(generics.ListCreateAPIView):
    queryset = OpenSystemsIntelVMWareSoftwareLicense.objects.all()
    serializer_class = OpenSystemsIntelVMWareSoftwareLicenseSerializer





class OpenSystemsIntelVirtualServerConfigurationListCreateView(generics.ListCreateAPIView):
    queryset = OpenSystemsIntelVirtualServerConfiguration.objects.all()
    serializer_class = OpenSystemsIntelVirtualServerConfigurationSerializer


class OpenSystemsIntelVirtualServerConfigurationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OpenSystemsIntelVirtualServerConfiguration.objects.all()
    serializer_class = OpenSystemsIntelVirtualServerConfigurationSerializer


class VirtualServerHardwarePriceListCreateView(generics.ListCreateAPIView):
    queryset = VirtualServerHardwarePrice.objects.all()
    serializer_class = VirtualServerHardwarePriceSerializer


class VirtualServerHardwarePriceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VirtualServerHardwarePrice.objects.all()
    serializer_class = VirtualServerHardwarePriceSerializer


class VirtualServerSoftwarePriceListCreateView(generics.ListCreateAPIView):
    queryset = VirtualServerSoftwarePrice.objects.all()
    serializer_class = VirtualServerSoftwarePriceSerializer


class VirtualServerSoftwarePriceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VirtualServerSoftwarePrice.objects.all()
    serializer_class = VirtualServerSoftwarePriceSerializer


class OpenSystemsIntelVirtualServerConfigurationCreateView(generics.CreateAPIView):
    serializer_class = OpenSystemsIntelVirtualServerConfigurationCreateSerializer


class OpenSystemsIntelVirtualServerConfigurationUpdateView(generics.UpdateAPIView):
    queryset = OpenSystemsIntelVirtualServerConfiguration.objects.all()
    serializer_class = OpenSystemsIntelVirtualServerConfigurationUpdateSerializer
