from django.contrib import admin
from .models import Contact, Product, Cart, CartItem, Order, OrderItem, Delivery

admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Delivery)