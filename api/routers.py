from rest_framework import routers

from api.views import CartViewSet, UserViewSet, CartItemViewSet, ProductViewSet

router = routers.DefaultRouter()

router.register(r'cart', CartViewSet)
router.register(r'user', UserViewSet)
router.register(r'cart-item', CartItemViewSet)
router.register(r'product', ProductViewSet)
