from rest_framework import serializers
from store.models import Cart, CartItem, Product, Order, User, DailyData


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', ]

    def create(self, validated_data):
        _user = validated_data.pop('user')
        user = User.objects.create_user(
            username=_user['username'],
            password=_user['password'],
            email=_user['email']
        )
        return user


class CartSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Cart
        fields = '__all__'

    def create(self, validated_data):
        _user = validated_data.pop('user')
        user = User.objects.create_user(username=_user['username'], email=_user['email'])
        cart = Cart.objects.create(user=user, **validated_data)
        return cart


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'
