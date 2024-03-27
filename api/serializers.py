from rest_framework import serializers
from store.models import Cart, CartItem, Product, Order, User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', ]


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
