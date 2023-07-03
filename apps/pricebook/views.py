# from .models import VirtualServer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
import math
from django_filters import rest_framework as filters
from .models import *
from .serializers import *


from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.core.exceptions import ObjectDoesNotExist
import logging

logger = logging.getLogger(__name__)



class VirtualServerCostFilter(filters.FilterSet):
    server_size_code = filters.CharFilter(field_name='server_size__code')

    class Meta:
        model = VirtualServerCost
        fields = ['server_size_code']


class SKUListCreateView(generics.ListCreateAPIView):
    queryset = SKU.objects.all()
    serializer_class = SKUSerializer


class SKUList(generics.ListAPIView):
    serializer_class = SKUSerializer

    def get_queryset(self):
        queryset = SKU.objects.all()
        sku_code = self.request.query_params.get('code')

        if sku_code is not None:
            queryset = queryset.filter(code=sku_code)
        return queryset


class SKUDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SKU.objects.all()
    serializer_class = SKUSerializer

    # def get_queryset(self):
    #     pk = self.kwargs['pk']
    #     return SKU.objects.filter(code=pk)


class VirtualServerSizeListCreate(generics.ListCreateAPIView):
    queryset = VirtualServerSize.objects.all()
    serializer_class = VirtualServerSizeSerializer


class VirtualServerCostListCreate(generics.ListCreateAPIView):
    queryset = VirtualServerCost.objects.all()
    serializer_class = VirtualServerCostSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = VirtualServerCostFilter


class ServerTypeListCreateView(generics.ListCreateAPIView):
    queryset = ServerType.objects.all()
    serializer_class = ServerTypeSerializer


class ServerTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = ServerType.objects.all()
    serializer_class = ServerTypeSerializer


class NetworkPricebookListCreateView(generics.ListCreateAPIView):
    queryset = NetworkPricebook.objects.all()
    serializer_class = NetworkPricebookSerializer


class NetworkPricebookListCreateViewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NetworkPricebook.objects.all()
    serializer_class = NetworkPricebookSerializer


class PriceBookListCreateView(generics.ListCreateAPIView):
    queryset = PriceBook.objects.all()
    serializer_class = PriceBookSerializer


class PriceBookRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = PriceBook.objects.all()
    serializer_class = PriceBookSerializer


#  This is for Calculations.


class SelectedVirtualServerCostView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        print("virtual server request data", request.data)

        try:
            num_cpus = request.data['virtual_server_size']['vcpu']
            print("Request", num_cpus)
            virtual_server_cost = num_cpus * 630
            hypervisor_cost = num_cpus * 550
            windows_os_cost = 606 * 1.5  # Assuming USD to SGD conversion rate is 1.5
            network_port_cost = num_cpus * 1000
            # total_cost = virtual_server_cost + hypervisor_cost + windows_os_cost
            response_data = [{

                "name": "Server Cost",
                "description": "Server Cost Virtual Serveran",
                "code": "virtual-server-server-cost",
                "price": virtual_server_cost,
                "cost_type":  "Hardware (CE)"
            },
                {

                "name": "Hypevisor Cost",
                "description": "Hypevisor Cost for Virtual Servers",
                "code": "virtual-server-hypervisor-cost",
                "price": hypervisor_cost,
                "cost_type":  "Hardware (CE)"

            },
                {
                "name": "Windows OS Cost",
                "description": "Windows OS Cost for Virtual Server",
                "code": "virtual-server-windows-os-cost",
                "price": windows_os_cost,
                "cost_type":  "Software (AE)"
            },

                {
                "name": "Network Post Cost",
                "description": "Network Port cost Virtual Server",
                "code": "Network port cost server",
                "price": network_port_cost,
                "cost_type":  "Hardware (CE)"
            }

            ]
            return Response(response_data)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class SelectedSanStorageCostView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            print("Storage data: request.data", request.data)
            san_storage_size = request.data.get('san_storage_size')
            san_storage_type = request.data.get('san_storage_type')
            print("Request payload", san_storage_size, san_storage_type)

            cost_multiplier = 0
            if san_storage_type == 'tier1':
                cost_multiplier = 7.80
            elif san_storage_type == 'tier2':
                cost_multiplier = 4.00

            # Calculate adjusted size including SAN and filesystem overheads
            overhead_ratio = 0.93  # 93% overhead for SAN and filesystem
            adjusted_capacity = round(
                san_storage_size / overhead_ratio / 5) * 5
            # Calculate purchase capacity as 50% of adjusted_capacity
            purchase_capacity = round(0.50 * adjusted_capacity)
            print("adjusted_capacity", adjusted_capacity)
            print("purchase_capacity", purchase_capacity)
            total_cost = round(purchase_capacity * cost_multiplier)

            response_data = {
                "name": "SAN Storage Cost",
                "description": "SAN Storage Cost",
                "code": "san-storage-cost",
                "price": total_cost,
                "storage_type": san_storage_type,
                "cost_type":  "Hardware (CE)"
            }

            print("response data", response_data)

            return Response(response_data)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class SelectedOperatingSystemCostView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        print("Operating System request data", request.data)

        try:
            operating_system = request.data['operating_system']['name']
            print("Request", operating_system)
            operating_system_cost = 5000
            operating_system_storage_cost = 100 * 10
            response_data = [
                {

                    "name": "Operating System Cost",
                    "description": "Operating System Cost",
                    "code": "operating-system-cost",
                    "price": operating_system_cost,
                    "cost_type":  "Software (AS)"
                },
                {

                    "name": "Operating System Storage Cost",
                    "description": "Operating Storage Cost",
                    "code": "operating-system-storage-cost",
                    "price": operating_system_storage_cost,
                    "cost_type":  "Hardware (CE)"

                }
            ]

            return Response(response_data)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class SelectedSanBackupStorageCostView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            # print("Backup Storage data: request.data", request.data )
            print("\033[32m Backup Storage data: \033[0m",
                  "\033[33m", request.data, "\033[0m")
            # app_san_storage_size = request.data.get('san_backup_storage_size')
            app_san_storage_size = request.data.get(
                'san_backup_storage_size', {}).get('totalSize')
            os_san_storage_size = 100

            environment = "SIT"

            cost_multiplier = 0
            if environment == 'PROD':
                cost_multiplier = 6
            elif environment == 'DR':
                cost_multiplier = 0
            else:
                cost_multiplier = 4

            total_san_backup_storage = app_san_storage_size + os_san_storage_size
            total_san_backup_storage_multiplier = total_san_backup_storage * cost_multiplier

            adjusted_capacity_ratio = 0.85
            adjusted_capacity = round(
                total_san_backup_storage_multiplier * adjusted_capacity_ratio)

            total_cost = round(adjusted_capacity * 1.32)

            response_data = {
                "name": "SAN Backup Storage Cost",
                "description": "SAN Backup Storage Cost",
                "code": "san-backup-storage-cost",
                "price": total_cost,
                "environment": "PROD",
                "cost_type":  "Hardware (CE)"
            }

            print("response data", response_data)

            return Response(response_data)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class OracleDBAppFileCostView(APIView):
    # permission classes later

    def post(self, request, *args, **kwargs):
        try:
            # print("Backup Storage data: request.data", request.data )
            print("\033[32m OracleDBAppFile Size data: \033[0m",
                  "\033[33m", request.data, "\033[0m")

            environment = request.data.get('environment')
            san_storage_type = request.data.get('san_storage_type')
            selected_disk_size = request.data.get('oracle_db_app_file_size')
            total_disk_size = selected_disk_size * 2

            cost_multiplier = 0
            if environment == 'PROD':
                cost_multiplier = 6
            elif environment == 'DR':
                cost_multiplier = 0
            else:
                cost_multiplier = 4

            print("total_disk_size", total_disk_size)
            # Calculate adjusted size including SAN and filesystem overheads
            overhead_ratio = 0.93
            value = (total_disk_size / (overhead_ratio) / 5)
            allocated_capacity = math.ceil(value) * 5
            purchase_capacity = math.ceil(allocated_capacity * 0.50)
            # 93% overhead for SAN and filesystem
            print("allocated capacity,", allocated_capacity)
            print("purchase_capacity", purchase_capacity)
            total_cost = round(purchase_capacity * cost_multiplier)

            remark = f"For environment {environment}, Storage tier :{san_storage_type}, Size Increased : {total_disk_size}  "

            response_data = [
                {
                    "name": "Oracle Database Application File - SAN Storage",
                    "description": "Oracle Database Application SAN Storage",
                    "code": "San Storage",
                    "size": total_disk_size,
                    "price": total_cost,
                    "cost_type": "Hardware CE",
                    "unit_price": 1.5,
                    "remark": remark,
                    "selected_size": selected_disk_size,
                    "purchase_capacity": purchase_capacity,
                    "allocated_capacity": allocated_capacity,
                },
                {
                    "name": "Oracle Database Application File - Backup SAN Storage",
                    "description": "Oracle Database Application Backup SAN Storage",
                    "code": "Backup San Storage",
                    "size": 100,
                    "price": 100,
                    "cost_type": "Hardware CE",
                    "unit_price": 10,
                    "remark": remark,
                    "purchase_capacity": 6000,
                    "allocated_capacity": 100,
                }
            ]

            print("response data", response_data)

            return Response(response_data)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class MsSqlDbTransLogView(APIView):
    # permission classes later

    def post(self, request, *args, **kwargs):
        try:
            print("\033[32m MsSqlDbTransLog Size data: \033[0m",
                  "\033[33m", request.data, "\033[0m")

            environment = request.data.get('environment')
            san_storage_type = request.data.get('san_storage_type')
            selected_disk_size = request.data.get('mssql_db_trans_log_size')
            san_storage_role_swap = request.data.get('san_storage_role_swap')
            total_disk_size = selected_disk_size * 2

            cost_multiplier = 0
            if environment == 'PROD':
                cost_multiplier = 6
            elif environment == 'DR':
                cost_multiplier = 0
            else:
                cost_multiplier = 4

            print("total_disk_size", total_disk_size)
            # Calculate adjusted size including SAN and filesystem overheads
            overhead_ratio = 0.93
            value = (total_disk_size / (overhead_ratio) / 5)
            allocated_capacity = math.ceil(value) * 5
            purchase_capacity = math.ceil(allocated_capacity * 0.50)
            # 93% overhead for SAN and filesystem
            print("allocated capacity,", allocated_capacity)
            print("purchase_capacity", purchase_capacity)
            total_cost = round(purchase_capacity * cost_multiplier)

            remark = f"For environment {environment}, Storage tier :{san_storage_type}, Role Swap: {san_storage_role_swap}, Size Increased : {total_disk_size}  "

            response_data = [
                {
                    "name": "MS SQL Database Trans and Log SAN Storage",
                    "description": "MS SQL Database Trans and Log SAN Storage",
                    "code": "San Storage",
                    "size": total_disk_size,
                    "price": total_cost,
                    "cost_type": "Hardware CE",
                    "unit_price": 1.5,
                    "remark": remark,
                    "selected_size": selected_disk_size,
                    "purchase_capacity": purchase_capacity,
                    "allocated_capacity": allocated_capacity,
                },
                {
                    "name": "MS SQL Database Trans and Log  - Backup SAN Storage",
                    "description": "MS SQL Database Trans and Log  Backup SAN Storage",
                    "code": "Backup San Storage",
                    "size": 100,
                    "price": 100,
                    "cost_type": "Hardware CE",
                    "unit_price": 10,
                    "remark": remark,
                    "purchase_capacity": 6000,
                    "allocated_capacity": 100,
                }
            ]

            print("response data", response_data)

            return Response(response_data)
        except Exception as e:
            return Response({'error': str(e)}, status=400)



class CalculateNasStorageCost(APIView):
    # permission classes later

    def post(self, request, *args, **kwargs):
        try:
            print("\033[32m NAS Storage Size data: \033[0m",
                  "\033[33m", request.data, "\033[0m")

            environment = request.data.get('environment')
            size = request.data.get('size')

            print("environment,size", environment, size)

            # Retrieve the NAS disk price from the Pricebook model
            try:
                nas_price = PriceBook.objects.get(code='NAS-DISK').price
                nas_backup_price = PriceBook.objects.get(code='BKUP-DISK').price
                print("nas_price", nas_price, nas_backup_price)

            except ObjectDoesNotExist:
                nas_price = 5.78
                nas_backup_price = 1.32

            # If the NAS disk price is not found in the Pricebook model,
            # use a default value of 5.78

            # Calculate NAS storage cost
            total_nas_disk_size = size
            total_nas_disk_cost = size * nas_price
            nas_remark = f"For environment {environment} and size {size}  with base price {nas_price}"

            cost_multiplier = 0
            if environment == 'PROD':
                cost_multiplier = 6
            elif environment == 'DR':
                cost_multiplier = 0
            else:
                cost_multiplier = 4

            # Calculate adjusted size for backup
            backup_usable_capacity = math.ceil(
                total_nas_disk_size * cost_multiplier)
            backup_purchase_capacity = math.ceil(backup_usable_capacity * 0.85)

            print("backup_usable_capacity,", backup_usable_capacity)
            print("backup_purchase_capacity", backup_purchase_capacity)

            total_backup_cost = round(
                backup_purchase_capacity * nas_backup_price)
            nas_backup_remark = f"For environment {environment} and size {backup_purchase_capacity}  with base price {nas_backup_price}"

            response_data = [
                {
                    "name": "NAS Storage",
                    "description": "NAS Storage",
                    "code": "NAS Storage",
                    "size": total_nas_disk_size,
                    "price": total_nas_disk_cost,
                    "cost_type": "Hardware CE",
                    "unit_price": nas_price,
                    "remark": nas_remark,
                },
                {
                    "name": "NAS Storage Backup",
                    "description": "NAS Storage Backup",
                    "code": "NAS Storage Backup",
                    "size": backup_purchase_capacity,
                    "price": total_backup_cost,
                    "cost_type": "Hardware CE",
                    "unit_price": nas_backup_price,
                    "remark": nas_backup_remark,
                }
            ]

            print("response data", response_data)

            return Response(response_data)
        # except Exception as e:
        #     return Response({'error': str(e)}, status=400)
        except Exception as e:
            logger.error('Error calculating NAS storage cost: %s', e, exc_info=True)
            return Response({'error': 'Error calculating NAS storage cost'}, status=400)


# New one here:
from .models import SanStorageOverhead, SanStorageRound, SanStorageCompression
from .serializers import SanStorageOverheadSerializer, SanStorageRoundSerializer, SanStorageCompressionSerializer

class SanStorageOverheadList(generics.ListCreateAPIView):
    queryset = SanStorageOverhead.objects.all()
    serializer_class = SanStorageOverheadSerializer

class SanStorageOverheadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SanStorageOverhead.objects.all()
    serializer_class = SanStorageOverheadSerializer

class SanStorageRoundList(generics.ListCreateAPIView):
    queryset = SanStorageRound.objects.all()
    serializer_class = SanStorageRoundSerializer

class SanStorageRoundDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SanStorageRound.objects.all()
    serializer_class = SanStorageRoundSerializer

class SanStorageCompressionList(generics.ListCreateAPIView):
    queryset = SanStorageCompression.objects.all()
    serializer_class = SanStorageCompressionSerializer

class SanStorageCompressionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SanStorageCompression.objects.all()
    serializer_class = SanStorageCompressionSerializer

from .models import SanStorageType, SanStoragePriceBook
from .serializers import SanStorageTypeSerializer, SanStoragePriceBookSerializer

class SanStorageTypeListCreate(generics.ListCreateAPIView):
    queryset = SanStorageType.objects.all()
    serializer_class = SanStorageTypeSerializer

class SanStoragePriceBookListCreate(generics.ListCreateAPIView):
    queryset = SanStoragePriceBook.objects.all()
    serializer_class = SanStoragePriceBookSerializer

class BackupStorageTypeListCreate(generics.ListCreateAPIView):
    queryset = BackupStorageType.objects.all()
    serializer_class = BackupStorageTypeSerializer


class BackupStoragePriceBookListCreate(generics.ListCreateAPIView):
    queryset = BackupStoragePriceBook.objects.all()
    serializer_class = BackupStoragePriceBookSerializer


# Vmware 


class VmwareServerOperatingSystemListCreate(generics.ListCreateAPIView):
    queryset = VmwareServerOperatingSystem.objects.all()
    serializer_class = VmwareServerOperatingSystemSerializer

class VmwareServerOperatingSystemStorageSizeListCreate(generics.ListCreateAPIView):
    queryset = VmwareServerOperatingSystemStorageSize.objects.all()
    serializer_class = VmwareServerOperatingSystemStorageSizeSerializer

class VmwareServerOperatingSystemPricebookListCreate(generics.ListCreateAPIView):
    queryset = VmwareServerOperatingSystemPriceBook.objects.all()
    serializer_class = VmwareServerOperatingSystemPriceBookSerializer

class CostTypeListCreate(generics.ListCreateAPIView):
    queryset = CostType.objects.all()
    serializer_class = CostTypeSerializer

class VmwareServerSizeListCreateView(generics.ListCreateAPIView):
    queryset = VmwareServerSize.objects.all()
    serializer_class = VmwareServerSizeSerializer

class VmwareServerSizeUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VmwareServerSize.objects.all()
    serializer_class = VmwareServerSizeSerializer

class VmwareServerPricebookListCreateView(generics.ListCreateAPIView):
    queryset = VmwareServerPricebook.objects.all()
    serializer_class = VmwareServerPricebookSerializer

class VmwareServerPricebookUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VmwareServerPricebook.objects.all()
    serializer_class = VmwareServerPricebookSerializer

class BigFixPricebookListCreateAPIView(generics.ListCreateAPIView):
    queryset = BigFixPricebook.objects.all()
    serializer_class = BigFixPricebookSerializer

class BigFixPricebookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BigFixPricebook.objects.all()
    serializer_class = BigFixPricebookSerializer