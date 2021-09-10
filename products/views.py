from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from products.models import Product
from products.serializers import ProductSerializer, ProductDetailSerializer


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        product_id = self.kwargs['pk']

        try:
            product = Product.objects.get(id=product_id)
            serializer = ProductDetailSerializer(product,context={"request": request})

            return Response(serializer.data)

        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
