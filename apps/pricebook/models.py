from django.db import models
from simple_history.models import HistoricalRecords



# Create your models here.

class CostType(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.id} - {self.name} - {self.code}"

class ServerType(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=100)
    description = models.TextField()
    

    def __str__(self):
        return f"{self.id} - {self.name} - {self.code}"



class VirtualServerSize(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=250)
    vcpu = models.IntegerField()
    ram_gb = models.IntegerField()
   

    def __str__(self):
        return f"{self.id} - {self.vcpu} vCPU, {self.ram_gb} GB RAM"
    

class VirtualServerNetworkCost(models.Model):
    server_type = models.ForeignKey(ServerType, on_delete=models.CASCADE, related_name='network_cost_server_type')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    code = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_type = models.ForeignKey(CostType, on_delete=models.PROTECT, related_name='network_cost_type')

    def __str__(self):
        return f"{self.id} - {self.name}, {self.server_type}"


class VirtualServerCost(models.Model):
    server_size = models.ForeignKey(VirtualServerSize, on_delete=models.PROTECT, related_name='virtual_server_cost')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    code = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_type = models.ForeignKey(CostType, on_delete=models.PROTECT, related_name='virtual_server_cost_type')

    def __str__(self):
        return f"{self.id} - {self.name} - {self.cost_type} - {self.server_size} Size"




class OsStorageCost(models.Model):
    server_size = models.ForeignKey(VirtualServerSize, on_delete=models.CASCADE, related_name='storage_cost')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    code = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_type = models.ForeignKey(CostType, on_delete=models.PROTECT, related_name='storage_cost_type')


class SKU(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_type = models.ForeignKey(CostType, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    history = HistoricalRecords()

class PriceBook(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_type = models.ForeignKey(CostType, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    server_type = models.ForeignKey(ServerType, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.id} - {self.name} - {self.code} - {self.price}"


class NetworkPricebook(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    code = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_type = models.ForeignKey(CostType, on_delete=models.PROTECT)
    server_type = models.ForeignKey(ServerType, on_delete=models.PROTECT)



    def __str__(self):
        return f"{self.id} - {self.name} - {self.code}"



# These are new one, 

class SanStorageOverhead(models.Model):
    overhead_ratio = models.FloatField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.overhead_ratio}-{self.description}"
    
class SanStorageRound(models.Model):
    round_to = models.PositiveIntegerField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.round_to}-{self.description}"
    

class SanStorageCompression(models.Model):
    compression_ratio = models.FloatField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.compression_ratio}-{self.description}"


class SanStorageType(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.code}"


class SanStoragePriceBook(models.Model):
    storage_type = models.OneToOneField(SanStorageType, on_delete=models.CASCADE, related_name='price_book')
    cost_type = models.ForeignKey(CostType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.storage_type} - {self.price} - {self.cost_type}"
    

class NasStoragePriceBook(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=100, unique=True)
    cost_type = models.ForeignKey(CostType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.storage_type} - {self.price} - {self.cost_type}"


class BackupStorageType(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.code}"


class BackupStoragePriceBook(models.Model):
    storage_type = models.OneToOneField(BackupStorageType, on_delete=models.CASCADE, related_name='price_book')
    cost_type = models.ForeignKey(CostType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.storage_type} - {self.price} - {self.cost_type}"

   

class BackupSanStorageMultiplier(models.Model):
    environment = models.CharField(max_length=255, unique=True)
    multiplier = models.FloatField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.environment} - {self.multiplier} - {self.description}"

    
class BackupSanStorageCostReductionMultiplier(models.Model):
    reduction_percentage = models.FloatField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.reduction_percentage} - {self.description}"
    
    
class BackupNasStorageMultiplier(models.Model):
    environment = models.CharField(max_length=255, unique=True)
    multiplier = models.FloatField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.environment} - {self.multiplier} - {self.description}"

class BackupNasStorageCostReductionMultiplier(models.Model):
    reduction_percentage = models.FloatField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.reduction_percentage} - {self.description}"
    
class VmwareServerOperatingSystem(models.Model):
    version = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.version} - {self.code}"

class VmwareServerOperatingSystemStorageSize(models.Model):
    version = models.ForeignKey(VmwareServerOperatingSystem, on_delete=models.CASCADE)
    storage_size = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.version} - {self.storage_size}"
    

class VmwareServerOperatingSystemPriceBook(models.Model):
    os = models.OneToOneField(VmwareServerOperatingSystem, on_delete=models.CASCADE, related_name='price_book')
    cost_type = models.ForeignKey(CostType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.os} - {self.price} - {self.cost_type}"
    

class VmwareServerSize(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=250)
    vcpu = models.IntegerField()
    ram_gb = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.id} - {self.vcpu} vCPU, {self.ram_gb} GB RAM"

class VmwareServerPricebook(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=250)
    cost_type = models.ForeignKey(CostType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} - {self.name} , {self.code}, {self.cost_type}, {self.price}"
    

class BigFixPricebook(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_type = models.ForeignKey(CostType, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name