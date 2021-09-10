from rest_framework import serializers
from users.models import UserBidConfig


class UserBidConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBidConfig
        fields = '__all__'
