from rest_framework import serializers
from Home.models import Cart, Orders
from django.contrib.auth.models import User
from Product.serializers import ProductSerializer



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ['user', 'products']

class OrdersSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Orders
        fields = ['products', 'address']

