from django.urls import path
from .views import (
    AssetCategoryListCreateView,
    AssetListCreateView,
    MaintenanceRecordListCreateView,
    EmployeeListCreateView,
    AssignmentListCreateView,
)

urlpatterns = [
    path('asset-categories/', AssetCategoryListCreateView.as_view(), name='asset-category-list-create'),
    path('assets/', AssetListCreateView.as_view(), name='asset-list-create'),
    path('maintenance-records/', MaintenanceRecordListCreateView.as_view(), name='maintenance-record-list-create'),
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('assignments/', AssignmentListCreateView.as_view(), name='assignment-list-create'),
]
