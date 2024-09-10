from django.contrib import admin
from . models import CartItem, OrderedItem, ContactMessage
# Register your models here.
admin.site.register(CartItem),
admin.site.register(OrderedItem),
admin.site.register(ContactMessage),