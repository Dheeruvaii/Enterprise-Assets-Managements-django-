# from django.shortcuts import render
# from rest_framework import viewsets

# # Create your views here.
# from rest_framework import generics
# from .models import AssetCategory, Asset, MaintenanceRecord, Employee, Assignment
# from .serializers import (
#     AssetCategorySerializer,
#     AssetSerializer,
#     MaintenanceRecordSerializer,
#     EmployeeSerializer,
#     AssignmentSerializer,
# )

# class AssetCategoryListCreateView(generics.ListCreateAPIView):
#     queryset = AssetCategory.objects.all()
#     serializer_class = AssetCategorySerializer

# class AssetCategoryListCreateView(viewsets.ModelViewSet):
#     queryset = AssetCategory.objects.all()
#     serializer_class = AssetCategorySerializer

# class AssetListCreateView(generics.ListCreateAPIView):


#     queryset = Asset.objects.all()
#     serializer_class = AssetSerializer
#     # filterset_class=AssetFilter

# class MaintenanceRecordListCreateView(generics.ListCreateAPIView):
#     queryset = MaintenanceRecord.objects.all()
#     serializer_class = MaintenanceRecordSerializer

# class EmployeeListCreateView(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class AssignmentListCreateView(generics.ListCreateAPIView):
#     queryset = Assignment.objects.all()
#     serializer_class = AssignmentSerializer
from django.shortcuts import render
from rest_framework import viewsets
from .models import AssetCategory, Asset, MaintenanceRecord, Employee, Assignment
from .serializers import (
    AssetCategorySerializer,
    AssetSerializer,
    MaintenanceRecordSerializer,
    EmployeeSerializer,
    AssignmentSerializer,
)

class AssetCategoryViewSet(viewsets.ModelViewSet):
    queryset = AssetCategory.objects.all()
    serializer_class = AssetCategorySerializer

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    filter_backends=[DjangoFilterBackendn]
    filterset_class=AssetFilter

class MaintenanceRecordViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRecord.objects.all()
    serializer_class = MaintenanceRecordSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
