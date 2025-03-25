from .models import PurchaseOrder, PurchaseOrderItem
from products.models import Item
import django_filters


class PurchaseOrderFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = PurchaseOrder
        fields = ['name']


class PurchaseOrderItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', field_name='item__name', label='items name')
    purchase_order = django_filters.CharFilter(lookup_expr='icontains', field_name='purchase_order__name', label='purchase orders name')

    class Meta:
        model = PurchaseOrderItem
        fields = ['purchase_order']