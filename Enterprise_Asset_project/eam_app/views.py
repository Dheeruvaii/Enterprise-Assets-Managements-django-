from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import AssetCategory, Asset, MaintenanceRecord, Employee, Assignment
from .serializers import (
    AssetCategorySerializer,
    AssetSerializer,
    MaintenanceRecordSerializer,
    EmployeeSerializer,
    AssignmentSerializer,
)

class AssetCategoryListCreateView(generics.ListCreateAPIView):
    queryset = AssetCategory.objects.all()
    serializer_class = AssetCategorySerializer

class AssetListCreateView(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class MaintenanceRecordListCreateView(generics.ListCreateAPIView):
    queryset = MaintenanceRecord.objects.all()
    serializer_class = MaintenanceRecordSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AssignmentListCreateView(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
