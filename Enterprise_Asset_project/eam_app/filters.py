# filters.py
import django_filters
from .models import Asset

class AssetFilter(django_filters.FilterSet):
    class Meta:
        model = Asset
        fields = {
            'name': ['exact', 'icontains'],
            'category__name': ['exact'],
            'acquisition_date': ['exact', 'gt', 'lt'],
            'purchase_cost': ['exact', 'gt', 'lt'],
            'location': ['exact', 'icontains'],
            'is_active': ['exact'],
        }
