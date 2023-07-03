from rest_framework import serializers
from .models import BillOfMaterial


class BillOfMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillOfMaterial
        fields = '__all__'

