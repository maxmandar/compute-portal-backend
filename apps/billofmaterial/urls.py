from django.urls import path
from .views import BillOfMaterialListCreateView, BillOfMaterialRetrieveUpdateDestroyView


urlpatterns = [
    path('billofmaterial/', BillOfMaterialListCreateView.as_view(), name='billofmaterial-list-create'),
    path('billofmaterial/<int:pk>/', BillOfMaterialRetrieveUpdateDestroyView.as_view(), name='billofmaterial-retrieve-update-destroy'),
]


