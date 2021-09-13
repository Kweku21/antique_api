from threading import Lock, Thread

from django.db.models import F
from products.models import Product, ProductBiding
from products.validators import validate_highest_user
from users.models import UserAutoBidProduct, UserBidConfig


class AutoBidBot:
    """
    Getting all users who have activated auto-bid for a product
    """

    def __init__(self, product: Product, amount: float):
        self.product = product
        self.amount = amount

    def get_users(self):
        users_auto_bid_products = (user.user for user in UserAutoBidProduct.objects.filter(product=self.product).all())
        return (user for user in users_auto_bid_products if self.get_user_with_enough_max_amount(user))

    def get_user_with_enough_max_amount(self, user) -> bool:
        user_bid_config = UserBidConfig.objects.filter(user=user).first()
        lock = Lock()
        with lock:
            if user_bid_config.max_bid_amount > 0 and (user_bid_config.max_bid_amount - self.amount + 1) > 0:
                UserBidConfig.objects.filter(user=user).update(max_bid_amount=F('max_bid_amount') - (self.amount + 1))
                return True
            else:
                return False

    def make_product_bid(self):
        for user in self.get_users():
            validate_highest_bid = validate_highest_user(user=user, product=self.product,
                                                         amount=self.amount + 1)

            if validate_highest_bid.get('status') is False:
                ProductBiding.objects.create(user=user, amount=self.amount + 1, product=self.product)

    def start_bot(self) -> None:
        thread = Thread(target=self.make_product_bid, daemon=True)
        thread.start()
