# serializers.py
from rest_framework import serializers
from .models import OracleDB

class OracleDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = OracleDB
        fields = '__all__'