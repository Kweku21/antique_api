from functools import wraps

from rest_framework import status
from rest_framework.response import Response

from products.models import Product, ProductBiding
from users.models import User


def add_product_bid_validator(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        data = request.data

        if len(data) == 0:
            return Response("All data is required to add a bid. Choose product and enter amount to continue",
                            status=status.HTTP_404_NOT_FOUND)
        elif data.get('user') is None:
            return Response("You are not authenticated to make a bid", status=status.HTTP_400_BAD_REQUEST)
        elif data.get('product') is None:
            return Response("Unknown Antique Product", status=status.HTTP_400_BAD_REQUEST)
        elif data.get('amount') is None and type(data.get('amount')) is not float:
            return Response("Invalid bid amount", status=status.HTTP_400_BAD_REQUEST)

        try:
            kwargs['product'] = Product.objects.get(id=data.get('product'))
        except Product.DoesNotExist:
            return Response("Product does not exist", status=status.HTTP_404_NOT_FOUND)

        validate_highest_bid = validate_highest_user(user=data.get('user'), product=kwargs['product'],
                                                     amount=data.get('amount'))
        if validate_highest_bid.get('status'):
            return Response(validate_highest_bid.get('message'), status=status.HTTP_400_BAD_REQUEST)

        return func(self, request, *args, **kwargs)
    return wrapper


def validate_highest_user(user: User, product: Product, amount: float) -> dict:

    highest_product_bid = ProductBiding.objects.filter(product=product).order_by('amount').first()
    if highest_product_bid.user == user:
        return dict(message="Your recent bid for this product is still the highest", status=True)

    last_user_bid = ProductBiding.objects.filter(product=product, user=user).last()
    if last_user_bid.amount == amount:
        return dict(message="Your last bid amount is the same as this amount", status=True)

    return dict(status=False)
