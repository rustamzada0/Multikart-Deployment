from django.contrib import admin
from .models import Orders, Cart, CartItem

# Register your models here.

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('variant', 'color', 'size', 'quantity', 'done', 'total_price')


class CartAdmin(admin.ModelAdmin):
    list_display = ('title','total_price',)
    list_display_links = ['title']


admin.site.register(Orders)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
