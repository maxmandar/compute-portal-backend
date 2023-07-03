from django.urls import path
from .views import EmployeeListCreateView, EmployeeRetrieveUpdateDestroy

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(),name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroy.as_view(),name='employee-list-create'),
]
