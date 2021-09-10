from django.db import models
from django.utils import timezone

from products.models import Product


class User:
    """
    Class representation of Users
    """
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return dict(name=self.name, email=self.email)


class UserBidConfig(models.Model):
    """
    Model for configuring auto-biding users
    """
    user = models.JSONField()
    max_bid_amount = models.FloatField()


class UserAutoBidProduct(models.Model):
    """
    Model for tracking all product which are configured to auto-bid by a user
    """
    user = models.JSONField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
