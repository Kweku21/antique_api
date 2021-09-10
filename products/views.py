from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet

from products.auto_bid_bot import AutoBidBot
from products.models import Product, ProductBiding
from products.serializers import ProductSerializer, ProductDetailSerializer, ProductBidSerializer
from products.validators import add_product_bid_validator


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        product_id = self.kwargs['pk']

        try:
            product = Product.objects.get(id=product_id)
            serializer = ProductDetailSerializer(product, context={"request": request})

            return Response(serializer.data)

        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ProductBidView(APIView):

    @add_product_bid_validator
    def post(self, request, **kwarg):
        data = request.data

        product = kwarg['product']
        product_bid = ProductBiding.objects.create(user=data.get('user'), amount=data.get('amount'),
                                                   product=product)

        # trigger auto biding bot
        auto_bid_bot = AutoBidBot(product=product, amount=product_bid.amount)
        auto_bid_bot.make_product_bid()

        serializer = ProductBidSerializer(product_bid)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

