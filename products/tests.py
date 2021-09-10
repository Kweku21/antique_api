import datetime

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from products.models import Product
from products.serializers import ProductSerializer, ProductDetailSerializer


class ProductViewsTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.products = [Product.objects.create(
            auction_date=datetime.datetime.now(),
            close_bid_date=datetime.datetime.now()
        ) for _ in range(2)]

        cls.product = cls.products[0]

    def test_can_browse_all_products(self):

        response = self.client.get(reverse("product-list"))

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(self.products), len(response.data['results']))

        for product in self.products:
            self.assertIn(
                ProductSerializer(instance=product).data,
                response.data['results']
            )

    def test_can_read_a_specific_product(self):
        response = self.client.get(
            reverse("single-product", args=[self.product.id])
        )

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(
            ProductDetailSerializer(instance=self.product).data,
            response.data
        )
