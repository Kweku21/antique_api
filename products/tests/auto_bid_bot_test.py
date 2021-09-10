from rest_framework.test import APITestCase
from django.utils import timezone
from products.auto_bid_bot import AutoBidBot
from products.models import Product, ProductBiding
from users.models import User, UserAutoBidProduct, UserBidConfig


class AutoBidBotTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.users = [
            User(name="Emmanuel Debrah", email="debrah@gmail.com"),
            User(name="Bismark Debrah", email="bismark@gmail.com"),
        ]

        cls.user = cls.users[0]

        cls.product = Product.objects.create(auction_date=timezone.now(),
                                             close_bid_date=timezone.now())

        # User Auto-Config Setup
        cls.user_auto_bid_config = UserBidConfig.objects.create(user=cls.users[0].__dict__, max_bid_amount=1000)

        cls.user_auto_bid_products = [
            UserAutoBidProduct.objects.create(user=cls.users[0].__dict__, product=cls.product)]

        cls.amount = 10.0

        cls.bid_bot = AutoBidBot(product=cls.product, amount=cls.amount)

    def test_get_users(self):
        self.assertEquals(self.bid_bot.get_users(), [self.user.__dict__])

    def test_make_product_bid(self):
        self.bid_bot.make_product_bid()

        product_bids = ProductBiding.objects.filter(user=self.user.__dict__).all()

        self.assertEquals(len(product_bids), 1)
        self.assertEquals(product_bids[0].amount, self.amount+1)
