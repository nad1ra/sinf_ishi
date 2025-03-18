from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from common.pagination import CustomPagination
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = ProductFilter
    filterset_fields = ['min_price', 'max_price']
    ordering_fields = ['price', 'created_at']
    search_fields = ['name', 'desc']