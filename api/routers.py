from rest_framework import routers

from api.views import CartViewSet, UserViewSet

router = routers.DefaultRouter()

router.register(r'cart', CartViewSet)
router.register(r'user', UserViewSet)
