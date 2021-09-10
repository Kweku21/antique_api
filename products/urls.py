from django.urls import path
from products.views import ProductView, ProductBidView

urlpatterns = [
    path('<int:pk>/', ProductView.as_view({'get': 'retrieve'}), name="single-product"),
    path('', ProductView.as_view({'get': 'list'}), name="product-list"),
    path('biding/', ProductBidView.as_view(http_method_names=['post']), name="product-bid")
]
