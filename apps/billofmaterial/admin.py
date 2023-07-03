from django.contrib import admin
from .models import BillOfMaterial

class BillOfMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'status')

admin.site.register(BillOfMaterial, BillOfMaterialAdmin)