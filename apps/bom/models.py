from django.db import models
# from project.models import Project
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from apps.pricebook.models import  SKU




    
    
class Environment(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.name} - {self.code}"
    


class BillOfMaterials(models.Model):
    project = models.ForeignKey('project.Project', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    # add more fields as required


class Datacenter(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return  f"{self.id} - {self.name} - {self.code}"
    
class Layer(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return  f"{self.id} - {self.name} - {self.code}"
    
class OperatingSystem(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.id} - {self.name} - {self.code} - {self.version}"
    
class Platform(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return  f"{self.id} - {self.name} - {self.code}"
    
class Model(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    description = models.TextField()
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE)

    def __str__(self):
        return  f"{self.id} - {self.name} - {self.code}"
    

class SANStorage(models.Model):
    storage_type = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    role_swap_required = models.BooleanField(default=False)

    def __str__(self):
        return  f"{self.id} - {self.storage_type} - {self.code}"


class Bom(models.Model):
    # project = models.ForeignKey(Project, on_delete=models.CASCADE)
    project = models.ForeignKey('project.Project', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return  f"{self.id} - {self.name}"


class BomItem(models.Model):
    bom = models.ForeignKey(Bom, on_delete=models.CASCADE, related_name='bom_items')
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.id} - {self.name}"


class BomItemConfig(models.Model):
    bom_item = models.ForeignKey(BomItem, on_delete=models.CASCADE, related_name='configurations')
    ram = models.PositiveIntegerField(null=True, blank=True)
    cores = models.PositiveIntegerField(null=True, blank=True)
    storage = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return  f"{self.id} - {self.name}"


class BomItemPricing(models.Model):
    bom_item = models.ForeignKey(BomItem, on_delete=models.CASCADE, related_name='pricing')
    software_price = models.DecimalField(max_digits=10, decimal_places=2)
    hardware_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return  f"{self.id} - {self.name}"


class OracleServer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return  f"{self.id} - {self.name}"


class PhysicalServer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return  f"{self.id} - {self.name}"
    


# Virtual Servers.

class OpenSystemsIntelVMWareSoftwareLicense(models.Model):
    bom_item = models.ForeignKey(BomItem, on_delete=models.CASCADE, related_name='open_systems_intel_vmware_software_licenses')
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE, related_name='open_systems_intel_vmware_software_licenses')

    def __str__(self):
        return f"{self.id} - {self.sku} - {self.bom_item}"

class OpenSystemsIntelVirtualServerConfiguration(models.Model):
    bom_item = models.OneToOneField('bom.BomItem', on_delete=models.CASCADE, related_name='virtual_server_configuration')
    environment = models.CharField(max_length=255)
    layer = models.CharField(max_length=255)
    server_details = models.CharField(max_length=255)
    cpu_count = models.IntegerField()
    memory_gb = models.DecimalField(max_digits=10, decimal_places=2)
    os_version = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    network_port_count = models.IntegerField()

    def __str__(self):
        return self.bom_item.name


class VirtualServerHardwarePrice(models.Model):
    configuration = models.OneToOneField(OpenSystemsIntelVirtualServerConfiguration, on_delete=models.CASCADE, related_name='hardware_price')
    hardware_cost = models.DecimalField(max_digits=10, decimal_places=2)
    ram_cost = models.DecimalField(max_digits=10, decimal_places=2)
    storage_san_cost = models.DecimalField(max_digits=10, decimal_places=2)
    backup_san_storage_cost = models.DecimalField(max_digits=10, decimal_places=2)
    nas_storage_cost = models.DecimalField(max_digits=10, decimal_places=2)
    san_port_cost = models.DecimalField(max_digits=10, decimal_places=2)
    network_port_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.configuration.bom_item.name


class VirtualServerSoftwarePrice(models.Model):
    configuration = models.OneToOneField(OpenSystemsIntelVirtualServerConfiguration, on_delete=models.CASCADE, related_name='software_price')
    ibm_pvu_count_cost = models.DecimalField(max_digits=10, decimal_places=2)
    tem_cost = models.DecimalField(max_digits=10, decimal_places=2)
    hypervisor_cost = models.DecimalField(max_digits=10, decimal_places=2)
    red_hat_os_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.configuration.bom_item.name
    
class ProfessionalServices(models.Model):
    configuration = models.OneToOneField(
        OpenSystemsIntelVirtualServerConfiguration,
        on_delete=models.CASCADE,
        related_name='professional_services'
    )
    service_name = models.CharField(max_length=255)
    service_description = models.TextField()
    service_price = models.DecimalField(max_digits=10, decimal_places=2)

class AdhocPrice(models.Model):
    configuration = models.OneToOneField(
        OpenSystemsIntelVirtualServerConfiguration,
        on_delete=models.CASCADE,
        related_name='adhoc_prices'
    )
    price_name = models.CharField(max_length=255)
    price_description = models.TextField()
    price_amount = models.DecimalField(max_digits=10, decimal_places=2)