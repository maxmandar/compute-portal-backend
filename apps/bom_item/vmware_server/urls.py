from django.urls import path
from .views import *


urlpatterns = [
    # path('list/', VmwareServerListView.as_view(), name='vmware-server-list'),
    # path('create/', VmwareServerCreateView.as_view(), name='vmware-server-create'),
    # path('validate/', validate_vmware_server_payload, name='validate_vmware_server_payload'),
    path('list/', VmwareServerListView.as_view(), name='vmware-server-list'),
    path('create/', VmwareServerCreateView.as_view(), name='vmware-server-create'),
    path('<int:pk>/big-fix-config-costs/', BigFixConfigCostsUpdateView.as_view(), name='big-fix-config-costs-update'),
    # path('detail/<int:pk>/', VmwareServerRetrieveUpdateDestroyView.as_view(), name='vmware-server-detail'),
]
