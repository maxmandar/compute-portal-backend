from django.urls import path
from .views import UserInfoView

urlpatterns = [
    # other URL patterns
    path('user-info/', UserInfoView.as_view(), name='user-info'),
]
