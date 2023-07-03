from django.contrib import admin

# Register your models here.

# Register your models here.
from django.contrib import admin
from .models import VirtualServer, VirtualServerSize, VirtualServerCost

admin.site.register(VirtualServer)
admin.site.register(VirtualServerSize)
admin.site.register(VirtualServerCost)