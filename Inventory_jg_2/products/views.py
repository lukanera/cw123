from rest_framework import viewsets
from .serializers import ItemSerializer, CategorySerializer
from .models import Item, Category
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ItemFilter


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class  = ItemFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
