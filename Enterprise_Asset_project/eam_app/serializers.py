
from rest_framework import serializers
from .models import *

class AssetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetCategory
        fields = ['id', 'name', 'description']

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['id', 'asset_number', 'name', 'category', 'acquisition_date', 'purchase_cost', 'current_value', 'location', 'is_active']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        category_data = {
                'id': instance.category.id,
                'name': instance.category.name,
            }
        representation['category'] = category_data

        return representation

class MaintenanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRecord
        fields = ['id', 'asset', 'maintenance_date', 'description', 'cost']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'department']


class AssignmentSerializer(serializers.ModelSerializer):
    # employee = EmployeeSerializer()  # Use the nested serializer for the employee field

    class Meta:
        model = Assignment
        fields = ['asset', 'employee', 'assignment_date', 'return_date']

    def to_representation(self, instance):
        representation= super().to_representation(instance)
        Employee_data ={
            'id':instance.employee.id,
            'name':instance.employee.name,
        }

        representation['employee']=Employee_data

        return representation