from django.urls import path
from .views import OpenSystemsIntelVMWareSoftwareLicenseListCreateView, EnvironmentListCreateView, LayerListCreateView

urlpatterns = [
    path('opensystems-intel-vmware-software-licenses/', OpenSystemsIntelVMWareSoftwareLicenseListCreateView.as_view(), name='opensystems_intel_vmware_software_licenses_list_create'),
]


from django.urls import path
from .views import (
    OpenSystemsIntelVirtualServerConfigurationListCreateView,
    OpenSystemsIntelVirtualServerConfigurationDetailView,
    VirtualServerHardwarePriceListCreateView,
    VirtualServerHardwarePriceDetailView,
    VirtualServerSoftwarePriceListCreateView,
    VirtualServerSoftwarePriceDetailView
)

urlpatterns = [
    path('api/virtual-server-configurations/', OpenSystemsIntelVirtualServerConfigurationListCreateView.as_view(), name='virtual_server_configuration_list_create'),
    path('api/virtual-server-configurations/<int:pk>/', OpenSystemsIntelVirtualServerConfigurationDetailView.as_view(), name='virtual_server_configuration_detail'),
    path('api/hardware-prices/', VirtualServerHardwarePriceListCreateView.as_view(), name='virtual_server_hardware_price_list_create'),
    path('api/hardware-prices/<int:pk>/', VirtualServerHardwarePriceDetailView.as_view(), name='virtual_server_hardware_price_detail'),
    path('api/software-prices/', VirtualServerSoftwarePriceListCreateView.as_view(), name='virtual_server_software_price_list_create'),
    path('api/software-prices/<int:pk>/', VirtualServerSoftwarePriceDetailView.as_view(), name='virtual_server_software_price_detail'),
    path('environment/', EnvironmentListCreateView.as_view(), name='environment_list_create'),
     path('layer/', LayerListCreateView.as_view(), name='layer_list_create'),
]
