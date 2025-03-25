from .models import SaleOrderItem, SaleOrder
import django_filters


class SaleOrderFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = SaleOrder
        fields = ['name']


class SaleOrderItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', field_name='item__name', label='items name')
    sale_order = django_filters.CharFilter(lookup_expr='icontains', field_name='sale_order__name', label='sale orders name')

    class Meta:
        model = SaleOrderItem
        fields = ['sale_order']