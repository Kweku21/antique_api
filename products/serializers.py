from rest_framework import serializers

from products.models import Product, ProductImage, ProductBiding


class ProductImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['id', 'image_url']

    def get_image_url(self, image):
        request = self.context.get('request')
        image_url = image.image.url
        return request.build_absolute_uri(image_url)


class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'created_at', 'product_images', 'price']


class ProductBidSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = ProductBiding
        fields = ['user', 'amount', 'product']


class ProductDetailSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True)
    product_biding = ProductBidSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'content', 'auction_date', 'price', 'product_biding',
                  'product_images', 'close_bid_date', 'created_at']
