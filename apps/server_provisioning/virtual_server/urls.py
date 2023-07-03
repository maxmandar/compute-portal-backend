from django.urls import path

from .views import VirtualServerCreateView, VirtualServerListView


urlpatterns = [
    path('virtual-server/', VirtualServerCreateView.as_view(), name='virtual_server_create'),
    path('virtual-server/list/', VirtualServerListView.as_view(), name='virtual_server_list'),
]
