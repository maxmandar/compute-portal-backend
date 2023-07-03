# from .models import VMwareServerSize, VirtualServerCost, NetworkCost, StorageCost, CostType
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
from .models import *
# Register your models here.

admin.site.register(CostType)
admin.site.register(ServerType)
admin.site.register(VirtualServerSize)
admin.site.register(VirtualServerCost)
admin.site.register(VirtualServerNetworkCost)
admin.site.register(OsStorageCost)
admin.site.register(PriceBook)
admin.site.register(SKU, SimpleHistoryAdmin)
admin.site.register(NetworkPricebook)

admin.site.register(SanStorageOverhead)
admin.site.register(SanStorageRound)
admin.site.register(SanStorageCompression)
admin.site.register(SanStorageType)
admin.site.register(SanStoragePriceBook)

admin.site.register(BackupStorageType)
admin.site.register(BackupStoragePriceBook)
admin.site.register(BackupSanStorageMultiplier)
admin.site.register(BackupSanStorageCostReductionMultiplier)

admin.site.register(VmwareServerSize)
admin.site.register(VmwareServerPricebook)
admin.site.register(VmwareServerOperatingSystem)
admin.site.register(VmwareServerOperatingSystemStorageSize)
admin.site.register(VmwareServerOperatingSystemPriceBook)
admin.site.register(BigFixPricebook)