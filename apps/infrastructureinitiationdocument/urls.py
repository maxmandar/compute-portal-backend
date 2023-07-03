from django.urls import path
from .views import IidProjectListCreateView, IidProjectRetrieveUpdateDestroyView

from .views import IidRequestorListCreate, IidRequestorRetrieveUpdateDestroy

urlpatterns = [
    path('iid-projects/', IidProjectListCreateView.as_view()),
    path('iid-projects/<int:pk>/', IidProjectRetrieveUpdateDestroyView.as_view()),
    path('iidrequestors/', IidRequestorListCreate.as_view()),
    path('iidrequestors/<int:pk>/', IidRequestorRetrieveUpdateDestroy.as_view()),
]


