from django.urls import path, include
from . import views

urlpatterns = [
    path('subcategory/<int:subcategory_id>', views.CategoryViewSet.as_view({'get': 'get_by_subcategory'})),
    path('categories/<int:category_id>/', views.ProductViewSet.as_view({'get': 'get_products_by_category'})),
    path('products/<int:pk>/', views.ProductViewSet.as_view({'get': 'get_by_id'})),
    path('products/<int:product_id>/reviews/create/', views.ReviewCreateView.as_view(), name='review_create'),
    path('products/<int:product_id>/reviews/', views.ReviewListView.as_view(), name='review_list'),
]
