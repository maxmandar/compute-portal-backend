from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import math
import traceback
import logging
import json

from .mixins import *
from apps.pricebook.models import *


logger = logging.getLogger(__name__)


class CalculateSanStorageCost(SanStorageCostMixin, APIView):
    # permission TBU

    def post(self, request, *args, **kwargs):
        try:
            print("\033[32m SAN Storage Cost Data: \033[0m",
                  "\033[33m", request.data, "\033[0m")

            request_data = request.data
            environment = request_data.get('environment')
            san_storage_type_code = request_data.get('sanStorageType')
            san_storage_size = request_data.get('sanStorageSize')
            role_swap_required = request_data.get('roleSwapRequired')
            san_storage_item = request_data.get('sanStorageItem')

            # Debugging print statements
            print("Environment:", environment)
            print("San storage type code:", san_storage_type_code)
            print("Role swap required:", role_swap_required)
            print("Requested disk size:", san_storage_size)
            # print("San Storage Item:", san_storage_item)

            # Calculate costs using mixin methods
            san_storage_config, san_storage_cost = self.calculate_san_storage_cost(
                san_storage_size, san_storage_type_code,san_storage_item)

            san_storage_role_swap_config, san_storage_role_swap_cost = self.calculate_role_swap_cost(
                san_storage_size, san_storage_type_code, role_swap_required, san_storage_item)

            san_storage_backup_config, san_storage_backup_cost = self.calculate_backup_cost(
                san_storage_size, environment, san_storage_item)

            # response_data = {
            #     san_storage_item: {
            #         "san_storage": san_storage_cost,
            #         "role_swap": san_storage_role_swap_cost,
            #         "san_storage_backup": san_storage_backup_cost
            #     }
            # }

            # print("response data", response_data)

            # san_storage_item = "app_binary_size"

            response_data = {

                "san_storage_config": san_storage_config,
                "san_storage_cost": san_storage_cost,
                "san_storage_role_swap_config": san_storage_role_swap_config,
                "san_storage_role_swap_cost": san_storage_role_swap_cost,
                "san_storage_backup_config": san_storage_backup_config,
                "san_storage_backup_cost": san_storage_backup_cost,

            }

            return Response(response_data)

            # response_data = {
            #     "os_config": os_config,
            #     "os_cost": [os_cost, os_san_storage_cost, os_san_storage_role_swap_cost]
            # }

        except Exception as e:
            logger.exception('Error calculating SAN storage cost for Application Binary')
            return Response({'error': f'Error calculating SAN storage cost for Application Binary: {str(e)}'}, status=400)


class CalculateSanStorageAppBinaryCost(SanStorageCostMixin, APIView):
    # permission TBU

    def post(self, request, *args, **kwargs):
        try:
            print("\033[32m Mandar SAN Storage Size App Binary Data: \033[0m",
                  "\033[33m", request.data, "\033[0m")

            request_data = request.data
            print("Request data:", request_data)
            environment = request_data.get('environment')
            san_storage_type_code = request_data.get('sanStorageType')
            requested_disk_size = request_data.get('appBinarySize')
            role_swap_required = request_data.get('roleSwapRequired')

            # Debugging print statements
            print("Environment:", environment)
            print("San storage type code:", san_storage_type_code)
            print("Requested disk size:", requested_disk_size)
            print("Role swap required:", role_swap_required)

            # Retrieve the NAS disk price from the Pricebook model

            # Calculate costs using mixin methods
            san_storage_costs = self.calculate_san_storage_cost(
                requested_disk_size, san_storage_type_code,"App Binarry")

            role_swap_costs = self.calculate_role_swap_cost(
                requested_disk_size, san_storage_type_code, role_swap_required)

            backup_costs = self.calculate_backup_cost(
                requested_disk_size, environment)

            response_data = {
                "san_storage_app_bin_cost": {
                    "san_storage": san_storage_costs,
                    "role_swap": role_swap_costs,
                    "san_storage_backup": backup_costs
                }
            }

            print("response data", response_data)

            return Response(response_data)

        except Exception as e:
            logger.exception('Error calculating SAN storage cost for Application Binary')
            return Response({'error': f'Error calculating SAN storage cost for Application Binary: {str(e)}'}, status=400)


class CalculateSanStorageAppDataLogCost(SanStorageCostMixin, APIView):
    # permission TBU

    def post(self, request, *args, **kwargs):
        try:
            print("\033[32m SAN Storage App Data and Log: \033[0m",
                  "\033[33m", request.data, "\033[0m")

            request_data = request.data
            print("Request data:", request_data)
            environment = request_data.get('environment')
            san_storage_type_code = request_data.get('sanStorageType')
            requested_disk_size = request_data.get('appDataLogSize')
            role_swap_required = request_data.get('roleSwapRequired')

            # Debugging print statements
            print("Environment:", environment)
            print("San storage type code:", san_storage_type_code)
            print("Requested disk size:", requested_disk_size)
            print("Role swap required:", role_swap_required)

            # Retrieve the NAS disk price from the Pricebook model

            # Calculate costs using mixin methods
            san_storage_costs = self.calculate_san_storage_cost(
                requested_disk_size, san_storage_type_code)
            role_swap_costs = self.calculate_role_swap_cost(
                requested_disk_size, san_storage_type_code, role_swap_required)
            backup_costs = self.calculate_backup_cost(
                requested_disk_size, environment)

            response_data = {
                "san_storage_app_data_log_cost": {
                    "san_storage": san_storage_costs,
                    "role_swap": role_swap_costs,
                    "san_storage_backup": backup_costs
                }
            }

            return Response(response_data)

            san_storage_config = {
                "os_version": os_code,
                "os_storage": os_storage_size,
                "os_san_storage_allocated_capacity": os_san_storage_config['requested_allocated_capacity'],
                "os_san_storage_purchase_capacity": os_san_storage_config['requested_purchase_capacity'],
                "os_san_storage_allocated_role_swap_capacity": os_san_storage_role_swap_config['role_swap_allocated_capacity'],
                "os_san_storage_allocated_role_swap_purchase_capacity": os_san_storage_role_swap_config['role_swap_allocated_capacity']

            }

            san_storage_cost = self.calculate_os_cost(os_code)

            response_data = {
                "os_config": os_config,
                "os_cost": [os_cost, os_san_storage_cost, os_san_storage_role_swap_cost]
            }

        except Exception as e:
            logger.exception('Error calculating SAN storage cost for Application Binary')
            return Response({'error': f'Error calculating SAN storage cost for Application Binary: {str(e)}'}, status=400)


class CalculateOperatingSystemCost(OSStorageSizeMixin, OSCostMixin, SanStorageCostMixin, APIView):

    def post(self, request):
        try:
            environment = request.data.get('environment')
            os_code = request.data.get('osCode')
            role_swap_required = request.data.get("roleSwapRequired", False)
            san_storage_type_code = request.data.get("sanStorageTypeCode")

            logger.debug(
                f"Input data: environment: {environment}, os_version: {os_code}, role_swap_required: {role_swap_required}, san_storage_type_code: {san_storage_type_code}")

            os_storage_size = self.get_os_storage_size(os_code)

            logger.info(f"os_storage_size:{os_storage_size}")

            os_san_storage_config, os_san_storage_cost = self.calculate_san_storage_cost( os_storage_size, san_storage_type_code, "Operating System")
            os_san_storage_role_swap_config, os_san_storage_role_swap_cost = self.calculate_role_swap_cost(os_storage_size, san_storage_type_code, role_swap_required, "Operating System")
            os_san_storage_backup_config, os_san_storage_backup_cost = self.calculate_backup_cost(os_storage_size, environment, "Operating System")

            os_config = {
                "os_version": os_code,
                # "os_storage": os_storage_size,
                # "os_san_storage_allocated_capacity": os_san_storage_config['requested_allocated_capacity'],
                # "os_san_storage_purchase_capacity": os_san_storage_config['requested_purchase_capacity'],
                # "os_san_storage_allocated_role_swap_capacity": os_san_storage_role_swap_config['role_swap_allocated_capacity'],
                # "os_san_storage_allocated_role_swap_purchase_capacity": os_san_storage_role_swap_config['role_swap_allocated_capacity']

            }

            os_cost = self.calculate_os_cost(os_code)

            response_data = {
                    "os_config": os_config,
                    "os_cost": os_cost,
                    "os_san_storage_config": os_san_storage_config,
                    "os_san_storage_cost": os_san_storage_cost,
                    "os_san_storage_role_swap_config": os_san_storage_role_swap_config,
                    "os_san_storage_role_swap_cost": os_san_storage_role_swap_cost,  
                    "os_san_storage_backup_config": os_san_storage_backup_config,
                    "os_san_storage_backup_cost": os_san_storage_backup_cost
                    }

            logger.info(f"Calculated response data: {response_data}")

            return Response(response_data)
        except Exception as e:
            logger.exception('Error calculating Operating System cost')
            return Response({'error': f'Error calculating Operating System cost: {str(e)}'}, status=400)


class CalculateVmwareServerSizeCost(VmWareServerSizeCostMixin, APIView):

    def post(self, request):
        try:
            vmware_server_cpu = request.data.get('vmwareServerSize').get('vcpu')
            vmware_server_ram = request.data.get('vmwareServerSize').get('ram_gb')

            logger.debug(f"Input data: vmware_server_cpu: {vmware_server_cpu}, vmware_server_ram: {vmware_server_ram}")

            vmware_server_size_config = {
                "vmware_server_cpu": vmware_server_cpu,
                "vmware_server_ram": vmware_server_ram,

            }

            vmware_server_size_cost = self.calculate_vmware_server_size_cost(vmware_server_cpu, vmware_server_ram)

            response_data = {
                "vmware_server_size_config": vmware_server_size_config,
                "vmware_server_size_cost": vmware_server_size_cost,

            }

            logger.info(f"Calculated response for vmware server size cost : {response_data}")

            return Response(response_data)
        except Exception as e:
            logger.exception('Error calculating Vmware Server Size Cost')
            return Response({'error': f'Error calculating Vmware Server Size Cost: {str(e)}'}, status=400)


class CalculateBigFixCost(BigFixCostMixin, APIView):

    def post(self, request):
        try:
            bigfix_required = request.data.get('is_bigfix_required', False)

            logger.debug(f"Input data: bigfix_required: {bigfix_required}")

            bigfix_cost = self.calculate_bigfix_cost(bigfix_required)

            bigfix_config = {
                "is_bigfix_required": bigfix_required
            }

            response_data = {
                "bigfix_config": bigfix_config,
                "bigfix_cost": bigfix_cost,
            }

            logger.info(f"Calculated response for BigFix cost: {response_data}")

            return Response(response_data)
        except Exception as e:
            logger.exception('Error calculating BigFix cost')
            return Response({'error': f'Error calculating BigFix cost: {str(e)}'}, status=400)
        


        
class CalculateVmwareServerAddRamCost(VmwareServerAddRamCostMixin, APIView):

    def post(self, request):
        try:
            add_ram_required = request.data.get('add_ram_required', False)

            logger.debug(f"Input data: add_ram_required: {add_ram_required}")

            vmware_cost = self.calculate_vmware_server_add_ram_cost(add_ram_required)

            vmware_config = {
                "add_ram_required": add_ram_required
            }

            response_data = {
                "vmware_server_extra_ram_config": vmware_config,
                "vmware_server_extra_ram_cost": vmware_cost,
            }

            logger.info(f"Calculated response for VMware Server Additional RAM cost: {response_data}")

            return Response(response_data)
        except Exception as e:
            logger.exception('Error calculating VMware Server Additional RAM cost')
            return Response({'error': f'Error calculating VMware Server Additional RAM cost: {str(e)}'}, status=400)
        

# class CalculateSanStorageAppBinaryCost(APIView):
#     # permission TBU

#     def post(self, request, *args, **kwargs):
#         try:
#             print("\033[32m SAN Storage Size App Binary Data: \033[0m",
#                   "\033[33m", request.data, "\033[0m")

#             environment = request.data.get('environment')
#             san_storage_type_code = request.data.get('sanStorageType')
#             requested_disk_size = request.data.get('appBinarySize')
#             role_swap_required = request.data.get('roleSwapRequired')

#             # Retrieve the NAS disk price from the Pricebook model

#             overhead_ratio = SanStorageOverhead.objects.first().overhead_ratio
#             round_to = SanStorageRound.objects.first().round_to
#             compression_ratio = SanStorageCompression.objects.first().compression_ratio
#             san_storage_price = PriceBook.objects.get(
#                 code=san_storage_type_code).price
#             san_backup_price = PriceBook.objects.get(code='BKUP-DISK').price

#             # Calculate Total Disk
#             value = (requested_disk_size / (overhead_ratio) / round_to)
#             requested_allocated_capacity = math.ceil(value) * round_to
#             requested_purchase_capacity = math.ceil(
#                 requested_allocated_capacity * compression_ratio)
#             requested_san_storage_cost = math.ceil(
#                 requested_purchase_capacity * san_storage_price)

#             # # If role swap is required, include RoleSwapDisk in the calculation
#             if role_swap_required:
#                 role_swap_allocated_capacity = requested_allocated_capacity
#                 role_swap_san_storage_cost = math.ceil(
#                     role_swap_allocated_capacity * san_storage_price)
#             else:
#                 role_swap_allocated_capacity = 0
#                 role_swap_san_storage_cost = 0

#             # Backup cost

#             backup_san_storage_multiplier = BackupSanStorageMultiplier.objects.get(
#                 environment=environment).multiplier
#             backup_compression_ratio = BackupSanStorageCostReductionMultiplier.objects.first(
#             ).reduction_percentage

#             # Calculate Backup Capacity and Cost
#             backup_multiplied_capacity = math.ceil(
#                 requested_disk_size * backup_san_storage_multiplier)
#             backup_purchase_capacity_reduced = math.ceil(
#                 backup_multiplied_capacity * backup_compression_ratio)

#             backup_san_storage_cost = math.ceil(
#                 backup_purchase_capacity_reduced * san_backup_price)

#             response_data = {
#                 "san_storage_app_bin_cost": {
#                     "san_storage": {
#                         "name": "SAN Storage",
#                         "description": "SAN Storage",
#                         "code": "san-storage",
#                         "size_requested_capacity": requested_disk_size,
#                         "size_allocated_capacity": requested_allocated_capacity,
#                         "size_purchase_capacity": requested_purchase_capacity,
#                         "cost": requested_san_storage_cost,
#                         "cost_type": "Hardware-CE",
#                         "unit_price": san_storage_price,
#                         "remark": ""
#                     },
#                     "role_swap": {
#                         "name": "Role Swap",
#                         "description": "Role Swap",
#                         "code": "san-storage",
#                         "size_requested_capacity": requested_disk_size,
#                         "size_allocated_capacity": role_swap_allocated_capacity,
#                         "cost": role_swap_san_storage_cost,
#                         "cost_type": "Hardware-CE",
#                         "unit_price": san_storage_price,
#                         "remark": ""
#                     },
#                     "san_storage_backup": {
#                         "name": "SAN Storage Backup",
#                         "description": "SAN Storage Backup",
#                         "code": "san-storage-backup",
#                         "size_requested_capacity": requested_disk_size,
#                         "size_multiplied_capacity": backup_multiplied_capacity,
#                         "size_purchase_capacity": backup_purchase_capacity_reduced,
#                         "price": backup_san_storage_cost,
#                         "cost_type": "Hardware-CE",
#                         "unit_price": san_backup_price,
#                         "remark": ""
#                     }
#                 }
#             }

#             print("response data", response_data)

#             return Response(response_data)

#         except Exception as e:
#             tb = traceback.format_exc()  # get the traceback as a string
#             return Response({'error': f'Error calculating SAN storage cost: {str(e)}\n\n{tb}'}, status=400)
