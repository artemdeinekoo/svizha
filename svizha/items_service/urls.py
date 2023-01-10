from django.urls import path, include
from . import views

urlpatterns = [
    path('categories/', views.CategoryViewSet.as_view({'get': 'list'})),
    path('categories/<int:category_id>/', views.ProductViewSet.as_view({'get': 'get_products_by_category'})),
    path('products/<int:pk>/', views.ProductViewSet.as_view({'get': 'get_by_id'}))
]
