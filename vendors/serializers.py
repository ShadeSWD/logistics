from rest_framework import serializers
from vendors.models import Dealer, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'model', 'release_date']


class DealerSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Dealer
        fields = ['name', 'email', 'country', 'city', 'street', 'house', 'building', 'letter', 'products']
