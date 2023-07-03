from django.shortcuts import render
from rest_framework import generics

from .models import OracleDB
from .serializers  import OracleDBSerializer

# Create your views here.
class OracleDBListCreateView(generics.ListCreateAPIView):
    queryset = OracleDB.objects.all()
    serializer_class = OracleDBSerializer


class OracleDBRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OracleDB.objects.all()
    serializer_class = OracleDBSerializer