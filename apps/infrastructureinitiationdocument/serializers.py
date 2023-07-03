from rest_framework import serializers
from .models import IidProject

from .models import IidRequestor




class IidRequestorSerializer(serializers.ModelSerializer):

    username = serializers.ReadOnlyField(source='requestor.username')
    
    class Meta:
        model = IidRequestor
        fields = '__all__'



class IidProjectSerializer(serializers.ModelSerializer):
    requestors = IidRequestorSerializer(many=True, read_only=True)

    class Meta:
        model = IidProject
        fields = '__all__'

