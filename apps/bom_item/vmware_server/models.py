from django.db import models
from apps.infrastructureinitiationdocument.models import IidProject
from apps.billofmaterial.models import BillOfMaterial


class BigFixConfig(models.Model):
    is_big_fix_required = models.BooleanField()
    vmware_server = models.OneToOneField('VmwareServer', on_delete=models.SET_NULL, null=True, related_name='big_fix_config')

    def __str__(self):
        return f"{'Required' if self.is_big_fix_required else 'Not Required'}"


class BigFixCost(models.Model):
    item = models.CharField(max_length=100)
    config = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    cost_type = models.CharField(max_length=100)
    vmware_server = models.ForeignKey('VmwareServer', on_delete=models.SET_NULL, null=True, related_name='big_fix_costs')

    def __str__(self):
        return f"{self.item}: {self.config} ({self.category}, {self.cost_type})"


class Application(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    vmware_server = models.ForeignKey('VmwareServer', on_delete=models.SET_NULL, null=True, related_name='applications')

    def __str__(self):
        return f"{self.name} ({self.code})"


class VmwareServerSizeConfig(models.Model):
    vmware_server_cpu = models.IntegerField()
    vmware_server_ram = models.IntegerField()
    vmware_server = models.ForeignKey('VmwareServer', on_delete=models.SET_NULL, null=True, related_name='vmware_server_size_configs')

    def __str__(self):
        return f"{self.vmware_server_cpu} vCPU, {self.vmware_server_ram} GB RAM"

class VmwareServerSizeCost(models.Model):
    item = models.CharField(max_length=100)
    config = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    cost_type = models.CharField(max_length=100)
    vmware_server = models.ForeignKey('VmwareServer', on_delete=models.SET_NULL, null=True, related_name='vmware_server_size_costs')

    def __str__(self):
        return f"{self.item}: {self.config} ({self.category}, {self.cost_type})"


class VmwareServer(models.Model):
    project = models.ForeignKey(IidProject, on_delete=models.CASCADE, related_name='vmware_servers')
    bom = models.ForeignKey(BillOfMaterial, on_delete=models.CASCADE, related_name='vmware_servers')
    requestor = models.CharField(max_length=100)
    environment = models.CharField(max_length=100)
    layer = models.CharField(max_length=100)
    hostname = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    clustering = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.hostname} ({self.platform}, {self.model})"