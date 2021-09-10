from rest_framework import serializers

from products.models import Product, ProductImage


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
        fields = ['name', 'created_at', 'product_images']


class ProductDetailSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True)
    product_biding = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = ['name', 'content', 'auction_date', 'product_biding',
                  'product_images', 'close_bid_date', 'created_at']
