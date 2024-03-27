from django.contrib import admin

from store.models import User, Product, CartItem, Cart, Order, DailyData

admin.site.register(User)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(DailyData)
