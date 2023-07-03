from django.urls import path
from .views import OracleDBListCreateView, OracleDBRetrieveUpdateDestroyView

urlpatterns = [
    path('', OracleDBListCreateView.as_view(), name='oracle-db-list-create'),
    path('<int:pk>/', OracleDBRetrieveUpdateDestroyView.as_view(), name='oracle-db-retrieve-update-destroy'),
]