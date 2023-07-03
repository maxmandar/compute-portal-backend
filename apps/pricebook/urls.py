from django.urls import path
# from .views import VirtualServerSizeListCreate, VirtualServerCostListCreate
# from .views import SKUList

# # classbased views
# from .views import SelectedVirtualServerCostView
# from .views import SelectedSanStorageCostView
# from .views import SelectedSanBackupStorageCostView

# from .views import OracleDBAppFileCostView
# from .views import MsSqlDbTransLogView

from .views import *

from .models import *

from .serializers import *


# from .views import PriceBookListCreateView, PriceBookRetrieveUpdateView
# from .views import NetworkSKUListCreateView, NetworkSKURetrieveUpdateDestroyView
# from .views import SKUListCreateView, SKUDetailView,  ServerTypeListCreateView, ServerTypeRetrieveUpdateDestroyView


# New one


urlpatterns = [

    path('virtualserversize/', VirtualServerSizeListCreate.as_view(), name='virtual-server-size'),
    path('virtualservercost/', VirtualServerCostListCreate.as_view(), name='virtual_server_size_list_create'),
    path('selected_virtual_server_cost/', SelectedVirtualServerCostView.as_view(), name='selected_virtual_server_cost'),
    path('selected_san_storage_cost/', SelectedSanStorageCostView.as_view(), name='selected_san_storage_cost'),
    path('selected_san_backup_storage_cost/', SelectedSanBackupStorageCostView.as_view(), name='selected_san_backup_storage_cost'),
    path('oracle_db_app_file_cost/', OracleDBAppFileCostView.as_view(), name='oracle_db_app_file_cost'),
    path('mssql_db_app_temp_cost/', MsSqlDbTransLogView.as_view(), name='mssql_db_app_temp_cost'),
    path('mssql_db_trans_log_cost/', MsSqlDbTransLogView.as_view(), name='mssql_db_trans_log_cost'),
    path('calculate-nas-storage-cost/',CalculateNasStorageCost.as_view(), name = 'calculate-nas-storage-cost'),
    path('san-storage-overhead/', SanStorageOverheadList.as_view(), name='san-storage-overhead-list'),
    path('san-storage-overhead/<int:pk>/', SanStorageOverheadDetail.as_view(), name='san-storage-overhead-detail'),
    path('san-storage-round/', SanStorageRoundList.as_view(), name='san-storage-round-list'),
    path('san-storage-round/<int:pk>/', SanStorageRoundDetail.as_view(), name='san-storage-round-detail'),
    path('vmware_server_os/', VmwareServerOperatingSystemListCreate.as_view(), name='vmware_server_os_size'),
    path('vmware_server_os_size/', VmwareServerOperatingSystemStorageSizeListCreate.as_view(), name='vmware_server_os_size'),
    path('vmware_server_os_pricebook/', VmwareServerOperatingSystemPricebookListCreate.as_view(), name='vmware_server_os_pricebook'),
    path('vmware_server_os_cost_type/', CostTypeListCreate.as_view(), name='vmware_server_os_cost_type'),
    path('san_storage_type/', SanStorageTypeListCreate.as_view(), name='san_storage_type'),
    path('san_storage_price_book/', SanStoragePriceBookListCreate.as_view(), name='san_storage_price_book'),
    path('backup-storage-types/', BackupStorageTypeListCreate.as_view(), name='backup-storage-type-list-create'),
    path('backup-storage-price-books/', BackupStoragePriceBookListCreate.as_view(), name='backup-storage-price-book-list-create'),
    path('vmware-server-size/', VmwareServerSizeListCreateView.as_view(), name='vmware_server_size_list_create'),
    path('vmware-server-size/<int:pk>/', VmwareServerSizeUpdateDestroyView.as_view(), name='vmware_server_size_update_destroy'),
    path('vmware-server-pricebook/', VmwareServerPricebookListCreateView.as_view(), name='vmware_server_pricebook_list_create'),
    path('vmware-server-pricebook/<int:pk>/', VmwareServerPricebookUpdateDestroyView.as_view(), name='vmware_server_pricebook_update_destroy'),
    path('bigfix-pricebook/', BigFixPricebookListCreateAPIView.as_view(), name='bigfix_pricebook_list_create'),
    path('bigfix-pricebook/<int:pk>/', BigFixPricebookRetrieveUpdateDestroyAPIView.as_view(), name='bigfix_pricebook_retrieve_update_destroy'),
    


]


