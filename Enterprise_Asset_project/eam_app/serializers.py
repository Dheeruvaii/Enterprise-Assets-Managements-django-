# from rest_framework import serializers
# from .models import AssetCategory, Asset, MaintenanceRecord, Employee, Assignment

# class AssetCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AssetCategory
#         fields = '__all__'

# class AssetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Asset
#         fields = '__all__'

# class MaintenanceRecordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MaintenanceRecord
#         fields = '__all__'

# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = '__all__'

# # class AssignmentSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Assignment
# #         fields = '__all__'
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

        # Check if 'employee' is a dictionary
        if 'employee' in representation and isinstance(representation['employee'], dict):
            # Extract the 'id' and 'name' fields from the nested serializer
            employee_data = {
                'id': instance.employee.id,
                'name': instance.employee.name,
            }
            representation['employee'] = employee_data

        return representation

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)

    #     # Check if 'category' is a dictionary
    #     if 'category' in representation and isinstance(representation['category'], dict):
    #         # Extract the 'name' field from the nested serializer
    #         category_name = representation['category']['name']
    #         representation['category'] = category_name

    #     return representation
        
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)

    #     # Extract the 'name' field from the nested serializer
    #     category_name = representation['category']['name']
    #     representation['category'] = category_name

    #     return representation
class MaintenanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRecord
        fields = ['id', 'asset', 'maintenance_date', 'description', 'cost']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'department']

# class AssignmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Assignment
#         fields = ['id', 'asset', 'employee', 'assignment_date', 'return_date']

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