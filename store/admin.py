from django.contrib import admin
from store.models import User, Product, CartItem

admin.site.register(User)
admin.site.register(Product)
admin.site.register(CartItem)
