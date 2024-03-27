from django.contrib import admin

from store.models import User, Product, CartItem, Cart, Order

admin.site.register(User)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order)
