from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from users.models import User, UserBidConfig
from users.serializers import UserBidConfigSerializer


class UserLoginTest(APITestCase):

    @classmethod
    def setUpTestData(cls):

        # Users Setup
        cls.users = [
            User(name="Emmanuel Debrah", email="debrah@gmail.com"),
            User(name="Bismark Debrah", email="bismark@gmail.com"),
        ]
        cls.user = cls.users[0]

        # User Auto-Config Setup
        cls.user_auto_bid_config = UserBidConfig.objects.create(user=cls.users[0].__dict__, max_bid_amount=1000)

    def test_login(self):
        response = self.client.post(reverse('login'), {})

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals({'user':self.user.__dict__,'bid_config':UserBidConfigSerializer(self.user_auto_bid_config).data}, response.data)

    def test_add_auto_bid_config(self):

        payload = {
            "user": {
                "name": "Bismark Debrah",
                "email": "bismark@gmail.com"
            },
            "amount": 1000
        }

        response = self.client.post(reverse("auto-bid-config"),format='json',data=payload)
        self.assertEquals(status.HTTP_201_CREATED, response.status_code)
        self.assertEquals({"message": "Successfully configured auto-build"}, response.data)
