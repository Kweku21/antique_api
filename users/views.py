from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User, UserBidConfig
from users.serializers import UserBidConfigSerializer
from users.validators import add_user_bid_config

default_users = [
    User(name="Emmanuel Debrah", email="debrah@gmail.com"),
    User(name="Bismark Debrah", email="bismark@gmail.com"),
]


class LoginView(APIView):
    """
    Login API View
    Dummy login logic
    """
    def post(self, request) -> Response:
        bid_config = UserBidConfig.objects.filter(user=default_users[0].__dict__).first()
        serializer = UserBidConfigSerializer(bid_config)
        return Response({'user': default_users[0].__dict__, 'bid_config': serializer.data}, status=status.HTTP_200_OK)


class UserAutoBidConfigView(APIView):
    """
    View to configure auto-bid
    """

    @add_user_bid_config
    def post(self, request) -> Response:
        data = request.data

        user_auto_bid_config = UserBidConfig.objects.create(user=data.get('user'), max_bid_amount=data.get('amount'))
        # serializer = UserBidConfigSerializer(user_auto_bid_config)

        return Response({"message": "Successfully configured auto-build"}, status=status.HTTP_201_CREATED)
