from .models import PurchaseOrder
from products.models import Item
import django_filters


class PurchaseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='', lookup_expr='icontains', label='items name')

    class Meta:
        model = PurchaseOrder
        fields = ['name']