from functools import wraps

from rest_framework import status
from rest_framework.response import Response

from users.models import UserBidConfig


def add_user_bid_config(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        data = request.data

        if len(data) == 0:
            return Response("All data is required to configure auto-bid. Enter maximum bid amount",
                            status=status.HTTP_404_NOT_FOUND)
        elif data.get('user') is None:
            return Response("You are not authenticated to configure an auto-bid", status=status.HTTP_400_BAD_REQUEST)
        elif data.get('amount') is None and type(data.get('amount')) is not float:
            return Response("Invalid bid amount", status=status.HTTP_400_BAD_REQUEST)

        auto_bid_config = UserBidConfig.objects.filter(user=data.get('user'))
        if auto_bid_config:
            return Response("Auto-Bid configuration already set for user", status=status.HTTP_400_BAD_REQUEST)

        return func(self, request, *args, **kwargs)
    return wrapper
