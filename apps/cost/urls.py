from django.urls import path
from .views import *
from .views_export import * 

urlpatterns = [
    # other URL patterns
     path('calculate-san-storage-cost/',CalculateSanStorageCost.as_view(), name = 'calculate-san-storage-cost'),
    path('calculate-san-storage-app-binary-cost/',CalculateSanStorageAppBinaryCost.as_view(), name = 'calculate-san-storage-app-binary-cost'),
    path('calculate-san-storage-app-data-log-cost/',CalculateSanStorageAppDataLogCost.as_view(), name = 'calculate-san-storage-app-data-log-cost'),
    path('calculate-os-cost/',CalculateOperatingSystemCost.as_view(), name = 'calculate-os-cost'),
    path('calculate-vmware-server-size-cost/',CalculateVmwareServerSizeCost.as_view(), name = 'calculate-vmware-server-size-cost'),
    path('calculate-bigfix-cost/',CalculateBigFixCost.as_view(), name = 'calculate-bigfix-cost'),
    path('calculate-vmware-server-add-ram-cost/',CalculateVmwareServerAddRamCost.as_view(), name = 'calculate-vmware-server-add-ram-cost'),
    path('export_excel/', ExportExcelView.as_view(), name='export_excel'),
    
]
