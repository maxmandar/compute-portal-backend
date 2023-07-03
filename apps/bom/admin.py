from django.contrib import admin

# Register your models here.
from .models import BillOfMaterials,Environment,Datacenter,Layer,SANStorage,Model,OperatingSystem, Platform, PhysicalServer, BomItemPricing,BomItemConfig

from .models import Bom, BomItem,OracleServer, OpenSystemsIntelVMWareSoftwareLicense

from .models import OpenSystemsIntelVirtualServerConfiguration, VirtualServerHardwarePrice, VirtualServerSoftwarePrice, ProfessionalServices, AdhocPrice


admin.site.register(BillOfMaterials)

admin.site.register(Environment)
admin.site.register(Datacenter)


admin.site.register(Layer)
admin.site.register(SANStorage)
admin.site.register(Model)

admin.site.register(OperatingSystem)
admin.site.register(Platform)

admin.site.register(PhysicalServer)
admin.site.register(BomItemPricing)
admin.site.register(BomItemConfig)
admin.site.register(Bom)
admin.site.register(BomItem)
admin.site.register(OracleServer)
admin.site.register(OpenSystemsIntelVMWareSoftwareLicense)




admin.site.register(OpenSystemsIntelVirtualServerConfiguration)
admin.site.register(VirtualServerHardwarePrice)
admin.site.register(VirtualServerSoftwarePrice)

admin.site.register(ProfessionalServices)
admin.site.register(AdhocPrice)