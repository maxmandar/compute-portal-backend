"""compute_portal_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    # include the URLs for the oauth2_provider app
    path('api/oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/', include('apps.project.urls')),
    path('api/', include('apps.iid.urls')),
    path('api/', include('apps.bom.urls')),
    path('api/', include('apps.employee.urls')),
    # path('api/application_catalogue/', include('apps.application_catalogue.urls')),
    # path('api/infrastructureinitiationdocument/', include('apps.infrastructureinitiationdocument.urls')),
    # path('api/pricebook/', include('apps.pricebook.urls')),
    # path('api/billofmaterial/', include('apps.billofmaterial.urls')),
    # path('api/server_provisioning/', include('apps.server_provisioning.virtual_server.urls')),
    # path('api/cost/', include('apps.cost.urls')),
    # path('api/bom-item/vmware-server/', include('apps.bom_item.vmware_server.urls')),
    # path('api/authentication/', include('apps.authentication.urls')),
    # path('api/', include('apps.billofmaterial.components.dbservers.oracledb.urls')),
]
