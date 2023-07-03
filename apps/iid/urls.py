from django.urls import path
from .views import SegmentListCreateView, SegmentRetrieveUpdateDestroyView
from .views import SubSegmentListCreateView, SubSegmentRetrieveUpdateDestroyView
from .views import IidListCreateView, IidRetrieveUpdateDestroyView

urlpatterns = [
    path('segments/', SegmentListCreateView.as_view(), name='segment-list-create'),
    path('segments/<int:pk>/', SegmentRetrieveUpdateDestroyView.as_view(), name='segment-detail'),
    path('sub-segments/', SubSegmentListCreateView.as_view(), name='sub-segment-list-create'),
    path('sub-segments/<int:pk>/', SubSegmentRetrieveUpdateDestroyView.as_view(), name='sub-segment-detail'),
    path('iid/', IidListCreateView.as_view(), name='iid-list-create'),
    path('iid/<int:pk>/', IidRetrieveUpdateDestroyView.as_view(), name='iid-retrieve-update-destroy'),
    
]
