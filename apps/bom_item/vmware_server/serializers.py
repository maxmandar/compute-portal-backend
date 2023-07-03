from rest_framework import serializers
from django.db import transaction
from .models import *

from rest_framework.exceptions import ValidationError

#  serializers for VmwareServer
class BigFixConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = BigFixConfig
        fields = '__all__'


class BigFixCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BigFixCost
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


class VmwareServerSizeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = VmwareServerSizeConfig
        fields = '__all__'


class VmwareServerSizeCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = VmwareServerSizeCost
        fields = '__all__'


# VmwareServer serializers for different views
class VmwareServerListSerializer(serializers.ModelSerializer):
    big_fix_config = BigFixConfigSerializer(read_only=True)
    big_fix_costs = BigFixCostSerializer(read_only=True, many=True)

    class Meta:
        model = VmwareServer
        fields = '__all__'

class VmwareServerCreateSerializer(serializers.ModelSerializer):
    big_fix_config = BigFixConfigSerializer()
    big_fix_costs = BigFixCostSerializer(many=True)

    class Meta:
        model = VmwareServer
        fields = '__all__'

    @transaction.atomic
    def create(self, validated_data):
        big_fix_config_data = validated_data.pop('big_fix_config')
        big_fix_costs_data = validated_data.pop('big_fix_costs')

        vmware_server = VmwareServer.objects.create(**validated_data)

        big_fix_config = BigFixConfig.objects.create(vmware_server=vmware_server, **big_fix_config_data)

        for big_fix_cost_data in big_fix_costs_data:
            BigFixCost.objects.create(vmware_server=vmware_server, **big_fix_cost_data)

        return vmware_server
    

class VmwareServerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VmwareServer
        fields = '__all__'


class BigFixConfigCostsUpdateSerializer(serializers.ModelSerializer):
    big_fix_config = BigFixConfigSerializer()
    big_fix_costs = BigFixCostSerializer(many=True)


    class Meta:
        model = VmwareServer
        fields = [ 'big_fix_config', 'big_fix_costs']

    def update(self, instance, validated_data):

        big_fix_costs_data_request = self.context['request'].data.get('big_fix_costs')
        print("big_fix_costs_data_request", big_fix_costs_data_request)
        big_fix_config_data = validated_data.get('big_fix_config')
        big_fix_costs_data = validated_data.get('big_fix_costs')

        print("big_fix_config", big_fix_config_data)
        print("big_fix_costs_data", big_fix_costs_data)

        # Update big_fix_config data
        big_fix_config = instance.big_fix_config
        if big_fix_config_data:
            big_fix_config.is_big_fix_required = big_fix_config_data.get('is_big_fix_required')
            big_fix_config.save()

         # Update big_fix_costs data
        existing_costs = instance.big_fix_costs.all()
        for cost_data_request in big_fix_costs_data_request:
            cost_id = cost_data_request.get('id')
            try:
                cost_instance = existing_costs.get(id=cost_id)
                cost_instance.item = cost_data_request.get('item')
                cost_instance.config = cost_data_request.get('config')
                cost_instance.category = cost_data_request.get('category')
                cost_instance.cost = cost_data_request.get('cost')
                cost_instance.cost_type = cost_data_request.get('cost_type')
                cost_instance.save()
            except BigFixCost.DoesNotExist:
                raise ValidationError(f"BigFixCost with ID {cost_id} does not exist for this VmwareServer.")

        return instance
