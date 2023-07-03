# Create your models here.
from django.db import models
from simple_history.models import HistoricalRecords

from apps.infrastructureinitiationdocument.models import IidProject
from apps.billofmaterial.models import BillOfMaterial


class Requestor(models.Model):
    name = models.CharField(max_length=255)

class Application(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.code}"

class OperatingSystem(models.Model):
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} {self.version}"
    
class OperatingSystemCost(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_type = models.CharField(max_length=255)

class VirtualServerSize(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    vcpu = models.IntegerField()
    ram_gb = models.IntegerField()

class VirtualServerCost(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_type = models.CharField(max_length=255)

class ServerCost(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_type = models.CharField(max_length=255)

class HypervisorCost(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_type = models.CharField(max_length=255)

class NetworkPortCost(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_type = models.CharField(max_length=255)




class VirtualServer(models.Model):
    project = models.ForeignKey(IidProject, on_delete=models.CASCADE)
    bom = models.ForeignKey(BillOfMaterial, on_delete=models.CASCADE)
    requestor = models.CharField(max_length=255)
    environment = models.CharField(max_length=255)
    layer = models.CharField(max_length=255)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    hostname = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    clustering = models.BooleanField()
    operating_system = models.ForeignKey(OperatingSystem, on_delete=models.CASCADE)
    operating_system_cost = models.ForeignKey(OperatingSystemCost, on_delete=models.CASCADE)
    size = models.ForeignKey(VirtualServerSize, on_delete=models.CASCADE)
    server_cost = models.ForeignKey(ServerCost, on_delete=models.CASCADE)
    hypervisor_cost = models.ForeignKey(HypervisorCost, on_delete=models.CASCADE)
    network_port_cost = models.ForeignKey(NetworkPortCost, on_delete=models.CASCADE)






# class OperatingSystemSanStorage(models.Model):
#     operating_system = models.OneToOneField(OperatingSystem, on_delete=models.CASCADE, related_name='os_san_storage')
#     size = models.IntegerField()
#     cost = models.DecimalField(max_digits=10, decimal_places=2)
#     cost_type = models.CharField(max_length=255)

# class ApplicationSanStorage(models.Model):
#     virtual_server = models.OneToOneField(VirtualServer, on_delete=models.CASCADE, related_name='app_san_storage')
#     binary_size = models.IntegerField()
#     data_log_size = models.IntegerField()
#     total_size = models.IntegerField()
#     san_storage_type = models.CharField(max_length=255)
#     san_storage_roll_swap = models.CharField(max_length=255)
#     cost = models.DecimalField(max_digits=10, decimal_places=2)
#     code = models.CharField(max_length=255)
#     cost_type = models.CharField(max_length=255)

# class SanBackupStorage(models.Model):
#     virtual_server = models.OneToOneField(VirtualServer, on_delete=models.CASCADE, related_name='san_backup_storage')
#     size = models.IntegerField()
#     adjusted_size = models.IntegerField()
#     cost = models.DecimalField(max_digits=10, decimal_places=2)
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     code = models.CharField(max_length=255)
#     cost_type = models.CharField(max_length=255)

# class ConnectDirect(models.Model):
#     virtual_server = models.OneToOneField(VirtualServer, on_delete=models.CASCADE, related_name='connect_direct')
#     name = models.CharField(max_length=255)
#     version = models.CharField(max_length=255)
#     quantity = models.IntegerField()
#     description = models.CharField(max_length=255)
#     cost = models.DecimalField(max_digits=10, decimal_places=2)
#     cost_type = models.CharField(max_length=255)

# class Bigfix(models.Model):
#     virtual_server = models.OneToOneField(VirtualServer, on_delete=models.CASCADE, related_name='bigfix')
#     name = models.CharField(max_length=255)
#     version = models.CharField(max_length=255)
#     quantity = models.IntegerField()
#     description = models.CharField(max_length=255)
#     cost = models.DecimalField(max_digits=10, decimal_places=2)
#     cost_type = models.CharField(max_length=255)