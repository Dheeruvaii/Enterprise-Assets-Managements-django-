 path('assignments/', AssignmentListCreateView.as_view(), name='assignment-list-create'),
# ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssetCategoryViewSet, AssetViewSet, MaintenanceRecordViewSet, EmployeeViewSet, AssignmentViewSet

router = DefaultRouter()
router.register(r'assetcategories', AssetCategoryViewSet, basename='assetcategory')
router.register(r'assets', AssetViewSet, basename='asset')
router.register(r'maintenancerecords', MaintenanceRecordViewSet, basename='maintenancerecord')
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'assignments', AssignmentViewSet, basename='assignment')

urlpatterns = [
    path('', include(router.urls)),
]
