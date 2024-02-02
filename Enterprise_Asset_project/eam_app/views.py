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
from django_filters.rest_framework import DjangoFilterBackend
from .filters import AssetFilter
# from filters import  *
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

    def create(self, request, *args, **kwargs):
        # Assuming your serializer is properly handling the request.data
        serializer = AssetCategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class=AssetFilter

    def create(self, request, *args, **kwargs):
        # Assuming your serializer is properly handling the request.data
        serializer = AssetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

class MaintenanceRecordViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRecord.objects.all()
    serializer_class = MaintenanceRecordSerializer

    
       
    def create(self, request, *args, **kwargs):
        # Assuming your serializer is properly handling the request.data
        serializer = MaintenanceRecordSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        # Assuming your serializer is properly handling the request.data
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    def create(self, request, *args, **kwargs):
        # Assuming your serializer is properly handling the request.data
        serializer = AssignmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)