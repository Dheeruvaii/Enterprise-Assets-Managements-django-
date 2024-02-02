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

     def create(self,instance):
        query=AssetCategory.objects.all()
        serializer=AssetCategorySerializer(query,many=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    filter_backends=[DjangoFilterBackend]
    # filterset_fields=AssetFilter

    def create(self,instance):
        query=Asset.objects.all()
        serializer=AssetSerializer(query,many=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

class MaintenanceRecordViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRecord.objects.all()
    serializer_class = MaintenanceRecordSerializer

    
       def create(self,instance):
        query=MaintenanceRecord.objects.all()
        serializer=MaintenanceRecordSerializer(query,many=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

       def create(self,instance):
        query=Employee.objects.all()
        serializer=EmployeeSerializer(query,many=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    def create(self,instance):
        query=Assignment.objects.all()
        serializer=AssignmentSerializer(query,many=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)