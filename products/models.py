from django.db import models
from django.utils import timezone


class Product(models.Model):
    """
    Model for storing antique products
    """
    name = models.CharField(max_length=100)
    content = models.TextField()
    price = models.FloatField(default=0.0)
    auction_date = models.DateTimeField()
    close_bid_date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    """
    Model for antique product images
    """
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_pics')
    created_at = models.DateTimeField(default=timezone.now)

    def __repr__(self):
        return dict(image=self.image.url)

    def __str__(self):
        return self.image.url


class ProductBiding(models.Model):
    """
    Model for antique product biding
    """
    product = models.ForeignKey(Product, related_name='product_biding', on_delete=models.CASCADE)
    user = models.JSONField()
    amount = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)

    def __repr__(self):
        return dict(amount=self.amount, user=self.user, product=self.product)
