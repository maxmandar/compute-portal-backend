import math
from math import ceil
import logging

from django.shortcuts import get_object_or_404
from apps.pricebook.models import *

logger = logging.getLogger(__name__)


class SanStorageCostMixin:

    def calculate_san_storage_cost(self, requested_disk_size, san_storage_type_code, item):
        try:

            logger.debug(f"Inside calculate_san_storage_cost SanStorageCostMixin")
            logger.debug(f"Requested Disk Size: {requested_disk_size}")

            overhead_ratio = SanStorageOverhead.objects.first().overhead_ratio
            logger.debug(f"Overhead Ratio: {overhead_ratio}")

            round_to = SanStorageRound.objects.first().round_to
            logger.debug(f"Round To: {round_to}")

            compression_ratio = SanStorageCompression.objects.first().compression_ratio
            logger.debug(f"Compression Ratio: {compression_ratio}")

            # san_storage_price = SanStorageType.objects.get(
            #     code=san_storage_type_code).price

            san_storage_object = get_object_or_404(SanStoragePriceBook, storage_type__code=san_storage_type_code)

            san_storage_price = san_storage_object.price
            san_storage_cost_type = san_storage_object.cost_type.name

            logger.debug(f"San Storage Price: {san_storage_price}")

            value = (requested_disk_size / (overhead_ratio) / round_to)
            requested_allocated_capacity = math.ceil(value) * round_to
            logger.debug(f"Allocated Capacity: {requested_allocated_capacity}")

            requested_purchase_capacity = math.ceil(
                requested_allocated_capacity * compression_ratio)
            logger.debug(f"Purchase Capacity: {requested_purchase_capacity}")

            requested_san_storage_cost = math.ceil(
                requested_purchase_capacity * san_storage_price)
            logger.debug(f"San Storage Cost: {requested_san_storage_cost}")

            result_config = {
                'san_storage_type': san_storage_type_code,
                'san_storage_size': requested_allocated_capacity,
                'san_storage_allocated_capacity': requested_allocated_capacity,
                'san_storage_purchase_capacity': requested_purchase_capacity,
            }

            result_cost = {
                "item": item,
                "config":f"{requested_allocated_capacity} GB for {san_storage_type_code} storage",
                "category": "San Storage Cost",
                "cost": requested_san_storage_cost,
                "type": san_storage_cost_type
            }

            return result_config, result_cost

        except Exception as e:
            logger.exception('Error calculating SAN storage cost')
            raise

    def calculate_role_swap_cost(self, requested_disk_size, san_storage_type_code, role_swap_required, item):
        overhead_ratio = SanStorageOverhead.objects.first().overhead_ratio
        round_to = SanStorageRound.objects.first().round_to
        # Role swap does not have compression.
        compression_ratio = SanStorageCompression.objects.first().compression_ratio

        value = (requested_disk_size / (overhead_ratio) / round_to)
        requested_allocated_capacity = math.ceil(value) * round_to
        san_storage_object = get_object_or_404(SanStoragePriceBook, storage_type__code=san_storage_type_code)

        san_storage_cost_type = san_storage_object.cost_type.name

        print("san_storage_object", san_storage_object)

        san_storage_price = san_storage_object.price

        print("san_storage_price", san_storage_price)
        if role_swap_required:
            role_swap_allocated_capacity = requested_allocated_capacity
            role_swap_san_storage_cost = math.ceil(
                role_swap_allocated_capacity * san_storage_price)
        else:
            role_swap_allocated_capacity = 0
            role_swap_san_storage_cost = 0

        # result = {
        #     'role_swap_allocated_capacity': role_swap_allocated_capacity,
        #     'role_swap_san_storage_cost': role_swap_san_storage_cost,
        # }

        # return result

        result_config = {
            'role_swap_allocated_capacity': role_swap_allocated_capacity,
            'role_swap_allocated_capacity': role_swap_allocated_capacity,
        }

        result_cost = {
            "item": item,
            "config":f"{role_swap_allocated_capacity} GB for {san_storage_type_code} storage",
            "category": "San Storage Cost for Role Swap",
            "cost": role_swap_san_storage_cost,
            "type": san_storage_cost_type
        }

        return result_config, result_cost

    def calculate_backup_cost(self, requested_disk_size, environment, item):
        backup_san_storage_multiplier = BackupSanStorageMultiplier.objects.get(
            environment=environment).multiplier
        backup_compression_ratio = BackupSanStorageCostReductionMultiplier.objects.first(
        ).reduction_percentage
        san_storage_backup_object = BackupStoragePriceBook.objects.get(
            storage_type__code='BACKUP_DISK')
        san_storage_backup_price = san_storage_backup_object.price
        san_storage_backup_cost_type = san_storage_backup_object.cost_type.name


        backup_multiplied_capacity = math.ceil(
            requested_disk_size * backup_san_storage_multiplier)
        backup_purchase_capacity_reduced = math.ceil(
            backup_multiplied_capacity * backup_compression_ratio)

        backup_san_storage_cost = math.ceil(
            backup_purchase_capacity_reduced * san_storage_backup_price)

        result_config = {
            'san_storage_backup_multiplied_capacity': backup_multiplied_capacity,
            'san_storage_backup_purchase_capacity_reduced': backup_purchase_capacity_reduced,
        }

        result_cost = {
            "item": item,
            "config":f"{backup_multiplied_capacity} GB for {environment} environment",
            "category": "San Storage Backup",
            "cost": backup_san_storage_cost,
            "type": san_storage_backup_cost_type
        }

        return result_config, result_cost


class OSStorageSizeMixin:

    def get_os_storage_size(self, os_code):
        try:
            logger.debug(f"Getting OS Storage for OS version: {os_code}")

            os_object = get_object_or_404(VmwareServerOperatingSystem, code=os_code)

            logger.debug(f"os_object: {os_object}")

            os_storage_size = VmwareServerOperatingSystemStorageSize.objects.get(
                version=os_object).storage_size
            logger.debug(f"os_storage_size: {os_storage_size}")

            logger.info(f"OS Storage Size data: {os_storage_size}")

            return os_storage_size

        except Exception as e:
            logger.exception('Error calculating Operating System Storage Size')
            raise


class OSCostMixin:

    def calculate_os_cost(self, os_code):
        try:
            logger.debug(f"Calculating OS cost for OS version: {os_code}")

            os_object = get_object_or_404(VmwareServerOperatingSystem, code=os_code)

            logger.debug(f"os_object: {os_object}")

            os_storage_size = VmwareServerOperatingSystemStorageSize.objects.get(
                version=os_object).storage_size
            logger.debug(f"os_storage_size: {os_storage_size}")

            pricebook_object = get_object_or_404(
                VmwareServerOperatingSystemPriceBook, os=os_object)

            logger.info(f"pricebook object: {pricebook_object}")

            os_cost = pricebook_object.price
            os_cost_type = pricebook_object.cost_type.name

            logger.info(f"os_cost_type: {os_cost_type}")

            logger.debug(
                f"os_object: {os_object}, os_storage_size: {os_storage_size}, os_version: {os_code}, os_price: {os_cost}")

            os_cost = {
                "item": "Operating System",
                "config": f"{os_code} Operating System",
                "category": "Operating System Cost",
                "cost": os_cost,
                "type": os_cost_type
            }

            logger.info(f"Calculated OS cost data: {os_cost}")

            return os_cost

        except Exception as e:
            logger.exception('Error calculating Operating System cost')
            raise




class VmWareServerSizeCostMixin:
    def calculate_vmware_server_size_cost(self, vmware_server_cpu, vmware_server_ram):
        try:
            logger.debug(f"Calculating Vmware Server Size Cost for: {vmware_server_cpu} vCPU and {vmware_server_ram} GB RAM")

            # Get the cost of Virtual Server, Hypervisor and Windows OS from the VmwareServerPricebook model
            virtual_server_pricebook = VmwareServerPricebook.objects.get(code='VMWARE_SERVER_VIRTUAL_SERVER_COST')
            hypervisor_pricebook = VmwareServerPricebook.objects.get(code='VMWARE_SERVER_HYPERVISOR_COST')
            windows_os_pricebook = VmwareServerPricebook.objects.get(code='VMWARE_SERVER_WINDOWS_OS_COST')
            network_port_pricebook = NetworkPricebook.objects.get(code='NETWORK_PORT_COST_VIRTUAL_SERVER')
            san_port_pricebook = NetworkPricebook.objects.get(code='SAN_PORT_COST_VIRTUAL_SERVER')
            

            virtual_server_price = virtual_server_pricebook.price
            hypervisor_price = hypervisor_pricebook.price
            windows_os_price = windows_os_pricebook.price
            network_port_price = network_port_pricebook.price
            san_port_price = san_port_pricebook.price

            virtual_server_cost_type = virtual_server_pricebook.cost_type.name
            hypervisor_cost_type = hypervisor_pricebook.cost_type.name
            windows_os_cost_type = windows_os_pricebook.cost_type.name
            network_port_cost_type = network_port_pricebook.cost_type.name
            san_port_cost_type = san_port_pricebook.cost_type.name

            logger.debug(f"virtual_server_price: {virtual_server_price}, hypervisor_price: {hypervisor_price}, windows_os_price: {windows_os_price}")

            # Calculate the total cost by multiplying the respective prices with the CPU and RAM of the server
            virtual_server_cost = ceil(float(virtual_server_price) * vmware_server_cpu)
            hypervisor_cost = ceil(float(hypervisor_price) * vmware_server_cpu)
            windows_os_cost = ceil(float(windows_os_price) * vmware_server_cpu)

            vmware_server_size_cost = [
                {
                    "item" : "Vmware Server",
                    "config": f"{vmware_server_cpu} vCPU, {vmware_server_ram} GB RAM",
                    "category": "Virtual Server Cost",
                    "cost": virtual_server_cost,
                    "type": virtual_server_cost_type
                },
                {
                    "item" : "Vmware Server",
                    "config": f"{vmware_server_cpu} vCPU, {vmware_server_ram} GB RAM",
                    "category": "Hypervisor Cost",
                    "cost": hypervisor_cost,
                    "type": hypervisor_cost_type

                },
                {
                    "item" : "Vmware Server",
                    "config": f"{vmware_server_cpu} vCPU, {vmware_server_ram} GB RAM",
                    "category": "Hypervisor Cost",
                    "cost": windows_os_cost,
                    "type": windows_os_cost_type
                },
                {
                    "item" : "Vmware Server",
                    "config": f"{vmware_server_cpu} vCPU, {vmware_server_ram} GB RAM",
                    "category": "Network Port Cost",
                    "cost": network_port_price,
                    "type": network_port_cost_type
                },
                {
                    "item" : "Vmware Server",
                    "config": f"{vmware_server_cpu} vCPU, {vmware_server_ram} GB RAM",
                    "category": "SAN Port Cost",
                    "cost": san_port_price,
                    "type": san_port_cost_type
                }
            ]

            
            logger.info(f"Calculated Vmware Server Size Cost: {vmware_server_size_cost}")

            return vmware_server_size_cost

        except Exception as e:
            logger.exception('Error calculating Vmware Server Size Cost')
            raise


class BigFixCostMixin:

    def calculate_bigfix_cost(self, bigfix_required):
        try:
            logger.debug(f"Calculating BigFix cost for BigFix required: {bigfix_required}")

            if bigfix_required:
                bigfix_pricebook = get_object_or_404(BigFixPricebook, code='BIG_FIX')
                bigfix_cost = bigfix_pricebook.price
                bigfix_cost_type = bigfix_pricebook.cost_type.name

            else:
                bigfix_cost = 0
                bigfix_cost_type = 'None'

            logger.debug(f"bigfix_required: {bigfix_required}, bigfix_cost: {bigfix_cost}, bigfix_cost_type: {bigfix_cost_type}")

            bigfix_cost_data = {
                "item": "Big Fix",
                "config": "Big Fix 1 License",
                "category": "Big Fix License Cost",
                "cost": bigfix_cost,
                "type": bigfix_cost_type
            }

            logger.info(f"Calculated BigFix cost data: {bigfix_cost_data}")

            return bigfix_cost_data

        except Exception as e:
            logger.exception('Error calculating BigFix cost')
            raise



class VmwareServerAddRamCostMixin:

    def calculate_vmware_server_add_ram_cost(self, add_ram_required):
        try:
            logger.debug(f"Calculating VMware Server Additional RAM cost for RAM addition required: {add_ram_required}")

            if add_ram_required:
                vmware_pricebook = get_object_or_404(VmwareServerPricebook, code='VMWARE_SERVER_ADD_RAM_64GB')
                vmware_cost = vmware_pricebook.price
                vmware_cost_type = vmware_pricebook.cost_type.name
            else:
                vmware_cost = 0
                vmware_cost_type = 'None'

            logger.debug(f"add_ram_required: {add_ram_required}, vmware_cost: {vmware_cost}, vmware_cost_type: {vmware_cost_type}")

            vmware_cost_data = {
                "item": "VMware Server",
                "config": "Additional RAM - 64GB",
                "category": "Additional RAM Cost",
                "cost": vmware_cost,
                "type": vmware_cost_type
            }

            logger.info(f"Calculated VMware Server Additional RAM cost data: {vmware_cost_data}")

            return vmware_cost_data

        except Exception as e:
            logger.exception('Error calculating VMware Server Additional RAM cost')
            raise