from datetime import date, timedelta

import django_filters
from django.utils.http import quote_etag

from .models import Item

class ItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")
    # in_stock = django_filters.BooleanFilter(field_name='stock_qty', lookup_expr='stock_qty__gt=0')
    in_stock = django_filters.BooleanFilter(field_name='stock_qty', method='in_stock_filter', label='in stock')

    def in_stock_filter(self, queryset, name, value):
        queryset = queryset.filter(stock_qty__gt=0)
        return queryset

    preorder = django_filters.BooleanFilter(field_name='stock_qty', method='preorder_filter', label='preorder')

    def preorder_filter(self, queryset, name, value):
        queryset = queryset.filter(stock_qty__lt=0)
        return queryset

    near_expiry = django_filters.BooleanFilter(field_name='expiration_date', method='near_expiry_filter', label='near_expiry')

    def near_expiry_filter(self, queryset, name, value):
        gt = date.today()
        lt = gt + timedelta(days=5)
        queryset = queryset.filter(expiration_date__gte=gt, expiration_date__lt=lt)
        return queryset

    class Meta:
        model = Item
        fields = ['name', 'description']