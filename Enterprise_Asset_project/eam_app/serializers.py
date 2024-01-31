from rest_framework import serializers
from .models import AssetCategory, Asset, MaintenanceRecord, Employee, Assignment

class AssetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetCategory
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class MaintenanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRecord
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

# class AssignmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Assignment
#         fields = '__all__'
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