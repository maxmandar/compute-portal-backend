from django.urls import path
from .views import *

urlpatterns = [
    path('projects/list/', ProjectListAPIView.as_view(), name='project-list'),
    path('projects/create/', ProjectCreateAPIView.as_view(), name='project-create'),
    path('projects/retrieve/<int:pk>/', ProjectRetrieveAPIView.as_view(), name='project-retrieve'),
    path('projects/update/<int:pk>/', ProjectUpdateAPIView.as_view(), name='project-update'),
    path('projects/destroy/<int:pk>/', ProjectDestroyAPIView.as_view(), name='project-destroy'),
    path('projects/<int:pk>/permissions/list/', ProjectPermissionListAPIView.as_view(), name='project-permission-list'),
    path('projects/<int:pk>/permissions/create/', ProjectPermissionCreateAPIView.as_view(), name='project-permission-create'),
    path('projects/<int:pk>/permissions/update/<int:permission_pk>/', ProjectPermissionUpdateAPIView.as_view(), name='project-permission-update'),
    path('projects/<int:pk>/permissions/destroy/<int:permission_pk>/', ProjectPermissionDestroyAPIView.as_view(), name='project-permission-destroy'),
    path('projects/user_roles/list/', UserRoleListAPIView.as_view(), name='project-user_role-list'),
    path('projects/user_roles/create/', UserRoleCreateAPIView.as_view(), name='project-user_role-create'),
    path('projects/user_roles/retrieve/<int:pk>/', UserRoleRetrieveAPIView.as_view(), name='project-user_role-retrieve'),
    path('projects/user_roles/update/<int:pk>/', UserRoleUpdateAPIView.as_view(), name='project-user_role-update'),
    path('projects/user_roles/destroy/<int:pk>/', UserRoleDestroyAPIView.as_view(), name='project-user_role-destroy'),
]
