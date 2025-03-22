from .models import SaleOrderItem
import django_filters


class SaleItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='item.name', lookup_expr='icontains')

    class Meta:
        model = SaleOrderItem
        fields = '__all__'