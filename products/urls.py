from django.urls import path
from products.views import ProductView

urlpatterns = [
    path('products/<int:pk>/', ProductView.as_view({'get': 'retrieve'}), name="single-product"),
    path('products/', ProductView.as_view({'get': 'list'}), name="product-list"),
]
