
from rest_framework import serializers

from .models import *


class VirtualServerSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualServerSize
        fields = '__all__'


class CostTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostType
        fields = '__all__'


class SKUSerializer(serializers.ModelSerializer):
    cost_type = CostTypeSerializer()

    class Meta:
        model = SKU
        fields = '__all__'



class ServerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerType
        fields = '__all__'


class NetworkPricebookSerializer(serializers.ModelSerializer):
    cost_type = CostTypeSerializer()
    server_type = ServerTypeSerializer()

    class Meta:
        model = NetworkPricebook
        fields = '__all__'


class PriceBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceBook
        fields = '__all__'


class VirtualServerCostSerializer(serializers.ModelSerializer):
    server_size = VirtualServerSizeSerializer()
    cost_type = CostTypeSerializer()

    class Meta:
        model = VirtualServerCost
        fields = '__all__'


class VirtualServerNetworkCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualServerNetworkCost
        fields = '__all__'


class OsStorageCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = OsStorageCost
        fields = '__all__'


class VirtualServerSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualServerSize
        fields = '__all__'


class VirtualServerCostSerializer(serializers.ModelSerializer):
    server_size = VirtualServerSizeSerializer()
    cost_type = CostTypeSerializer()


    class Meta:
        model = VirtualServerCost
        fields = '__all__'


# New one here:

from .models import SanStorageOverhead, SanStorageRound, SanStorageCompression

class SanStorageOverheadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SanStorageOverhead
        fields = '__all__'

class SanStorageRoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = SanStorageRound
        fields = '__all__'

class SanStorageCompressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SanStorageCompression
        fields = '__all__'

from .models import SanStorageType, SanStoragePriceBook

class SanStorageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SanStorageType
        fields = '__all__'


class SanStoragePriceBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = SanStoragePriceBook
        fields = '__all__'


# serializers.py
class BackupStorageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackupStorageType
        fields = '__all__'


class BackupStoragePriceBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackupStoragePriceBook
        fields = '__all__'



# For NAS Strorage

class NasStoragePriceBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = NasStoragePriceBook
        fields = '__all__'


# For VMWARE 



class VmwareServerOperatingSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VmwareServerOperatingSystem
        fields = '__all__'

class VmwareServerOperatingSystemStorageSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VmwareServerOperatingSystemStorageSize
        fields = '__all__'

class CostTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostType
        fields = '__all__'

class VmwareServerOperatingSystemPriceBookSerializer(serializers.ModelSerializer):
    cost_type = CostTypeSerializer(read_only=True)
    os = VmwareServerOperatingSystemSerializer(read_only=True)

    class Meta:
        model = VmwareServerOperatingSystemPriceBook
        fields = '__all__'

class VmwareServerSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VmwareServerSize
        fields = '__all__'

class VmwareServerPricebookSerializer(serializers.ModelSerializer):
    cost_type = CostTypeSerializer(read_only=True)
    
    class Meta:
        model = VmwareServerPricebook
        fields = '__all__'

class BigFixPricebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BigFixPricebook
        fields = '__all__'