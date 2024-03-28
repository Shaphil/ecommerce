from rest_framework import routers

from api.views import CartViewSet, UserViewSet, CartItemViewSet, ProductViewSet, OrderViewSet, DailyDataViewSet

router = routers.DefaultRouter()

router.register(r'cart', CartViewSet)
router.register(r'user', UserViewSet)
router.register(r'cart-item', CartItemViewSet)
router.register(r'product', ProductViewSet)
router.register(r'order', OrderViewSet)
router.register(r'daily-data', DailyDataViewSet)
