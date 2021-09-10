from django.utils import timezone
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from products.models import Product, ProductBiding
from products.serializers import ProductSerializer, ProductDetailSerializer, ProductBidSerializer
from users.models import User


class ProductViewsTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # Products Setup
        cls.products = [Product.objects.create(
            auction_date=timezone.now(),
            close_bid_date=timezone.now()
        ) for _ in range(4)]

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


class ProductBidViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.users = [
            User(name="Emmanuel Debrah", email="debrah@gmail.com"),
            User(name="Bismark Debrah", email="bismark@gmail.com"),
        ]

        cls.user = cls.users[0]

        cls.product = Product.objects.create(auction_date=timezone.now(),
                                             close_bid_date=timezone.now())

        cls.product_bid = ProductBiding.objects.create(user=cls.users[1].__dict__, amount=100,
                                                   product=cls.product)

    def test_add_product_bid(self):
        payload = {
            "user": {
                "name": "Emmanuel Debrah",
                "email": "debrah@gmail.com"
            },
            "product": "1",
            "amount": 40.50
        }

        response = self.client.post(reverse("product-bid"), format='json', data=payload)
        self.assertEquals(status.HTTP_201_CREATED, response.status_code)

