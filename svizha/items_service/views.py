from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size = 20


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ('title', 'price')

    def get_by_id(self, request, pk=None):
        """
        Отримати товар по id.
        """
        product = self.queryset.get(pk=pk)
        serializer = self.get_serializer(product)
        return Response(serializer.data)

    def get_products_by_category(self, request, category_id):
        """
        Отримати товари однієї категорії.
        """
        products = self.queryset.filter(category=category_id)
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data)

