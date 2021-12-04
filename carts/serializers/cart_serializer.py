from rest_framework import serializers
from carts.models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = serializers.ALL_FIELDS
