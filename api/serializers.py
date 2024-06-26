from rest_framework import serializers
from store.models import Cart, CartItem, Product, Order, User, DailyData


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

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
    # user = UserSerializer()

    class Meta:
        model = Cart
        fields = '__all__'

    # def create(self, validated_data):
    #     _user = validated_data.pop('user')
    #     user = User.objects.create_user(username=_user['username'], email=_user['email'])
    #     cart = Cart.objects.create(user=user, **validated_data)
    #     return cart


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        name = validated_data.pop('name')
        price = validated_data.pop('price')
        image = validated_data.pop('image')
        product = Product.objects.create(name=name, price=price, image=image)
        return product


class ProductGetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    # product = ProductGetSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'

    # def create(self, validated_data):
    #     product = validated_data.pop('product')
    #     quantity = validated_data.pop('quantity')
    #     price = validated_data.pop('price')
    #     cart = validated_data.pop('cart')
    #     cart_item = CartItem.objects.create(
    #         product=product,
    #         quantity=quantity,
    #         price=price,
    #         cart=cart
    #     )
    #     return cart_item


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    # cart = CartSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class DailyDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DailyData
        fields = '__all__'
