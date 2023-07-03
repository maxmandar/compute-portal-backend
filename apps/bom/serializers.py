from rest_framework import serializers
from .models import Environment,Datacenter, Layer, OperatingSystem, Platform, Model,SANStorage, Bom,BomItem
from .models import OpenSystemsIntelVMWareSoftwareLicense
from apps.pricebook.serializers import SKUSerializer
from .models import OpenSystemsIntelVirtualServerConfiguration, VirtualServerHardwarePrice, VirtualServerSoftwarePrice, AdhocPrice, ProfessionalServices


class BomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bom
        fields = '__all__'

class BomItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BomItem
        fields = '__all__'
        
class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = '__all__'


class DatacenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datacenter
        fields = '__all__'

class LayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layer
        fields = '__all__'


class OperatingSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatingSystem
        fields = ['id', 'name', 'version']



class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'

class SANStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SANStorage
        fields = '__all__'



class OpenSystemsIntelVMWareSoftwareLicenseSerializer(serializers.ModelSerializer):
    bom_item = BomItemSerializer()
    sku = SKUSerializer()

    class Meta:
        model = OpenSystemsIntelVMWareSoftwareLicense
        fields = '__all__'





class VirtualServerHardwarePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualServerHardwarePrice
        fields = '__all__'


class VirtualServerSoftwarePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualServerSoftwarePrice
        fields = '__all__'
# serializers.py

class ProfessionalServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalServices
        fields = '__all__'


class AdhocPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdhocPrice
        fields = '__all__'

class OpenSystemsIntelVirtualServerConfigurationSerializer(serializers.ModelSerializer):
    hardware_price = VirtualServerHardwarePriceSerializer()
    software_price = VirtualServerSoftwarePriceSerializer()
    adhoc_prices = AdhocPriceSerializer()


    class Meta:
        model = OpenSystemsIntelVirtualServerConfiguration
        fields = '__all__'


class OpenSystemsIntelVirtualServerConfigurationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenSystemsIntelVirtualServerConfiguration
        fields = '__all__'


class OpenSystemsIntelVirtualServerConfigurationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenSystemsIntelVirtualServerConfiguration
        fields = '__all__'

