from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer
from .models import Category, Product, Review
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size = 20


class OneElementPagination(PageNumberPagination):
    page_size = 1


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_by_subcategory(self, request, subcategory_id):
        categories = self.queryset.filter(subcategory_id=subcategory_id)
        serializer = self.serializer_class(categories, many=True)
        return Response(serializer.data)


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


class ReviewCreateView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = OneElementPagination
