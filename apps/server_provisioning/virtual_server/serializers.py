from rest_framework import serializers
from django.db import transaction
from .models import (
    Requestor, Application, OperatingSystem, VirtualServer,
    VirtualServerSize, VirtualServerCost, OperatingSystemCost,
    ServerCost, HypervisorCost, NetworkPortCost
)

class ServerCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerCost
        fields = '__all__'

class HypervisorCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = HypervisorCost
        fields = '__all__'

class NetworkPortCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkPortCost
        fields = '__all__'


class RequestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requestor
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class OperatingSystemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OperatingSystem
        fields = ['name', 'version', 'description']
        

class OperatingSystemCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatingSystemCost
        fields = '__all__'

class VirtualServerSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualServerSize
        fields = ['name', 'code', 'vcpu', 'ram_gb']

class VirtualServerCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualServerCost
        fields = ['name', 'description', 'code', 'price', 'cost_type']


class VirtualServerSerializer(serializers.ModelSerializer):
    application = ApplicationSerializer()
    operating_system = OperatingSystemSerializer()
    operating_system_cost = OperatingSystemCostSerializer()
    size = VirtualServerSizeSerializer()
    server_cost = ServerCostSerializer()
    hypervisor_cost = HypervisorCostSerializer()
    network_port_cost = NetworkPortCostSerializer()

    class Meta:
        model = VirtualServer
        fields = [
            'project', 'bom', 'requestor', 'environment', 'layer', 'application',
            'hostname', 'platform', 'model', 'clustering', 'operating_system',
            'operating_system_cost', 'size',
            'server_cost', 'hypervisor_cost', 'network_port_cost'
        ]

    @transaction.atomic
    def create(self, validated_data):
        application_data = validated_data.pop('application')
        operating_system_data = validated_data.pop('operating_system')
        operating_system_cost_data = validated_data.pop('operating_system_cost')
        size_data = validated_data.pop('size')
        server_cost_data = validated_data.pop('server_cost')
        hypervisor_cost_data = validated_data.pop('hypervisor_cost')
        network_port_cost_data = validated_data.pop('network_port_cost')       

        application = Application.objects.create(**application_data)
        operating_system = OperatingSystem.objects.create(**operating_system_data)
        operating_system_cost = OperatingSystemCost.objects.create(**operating_system_cost_data)
        size = VirtualServerSize.objects.create(**size_data)
        server_cost = ServerCost.objects.create(**server_cost_data)
        hypervisor_cost = HypervisorCost.objects.create(**hypervisor_cost_data)
        network_port_cost = NetworkPortCost.objects.create(**network_port_cost_data)

        virtual_server = VirtualServer.objects.create(
            application=application,
            operating_system=operating_system,
            operating_system_cost=operating_system_cost,
            size=size,
            server_cost=server_cost,
            hypervisor_cost=hypervisor_cost,
            network_port_cost=network_port_cost,
            **validated_data
        )

        return virtual_server

