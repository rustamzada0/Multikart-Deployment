from django.contrib import admin
from .models import *

# Register your models here.

class WishListAdmin(admin.ModelAdmin):
    list_display = ['title', 'user_id', 'username', 'product_photo']
    list_display_links = ['title', 'product_photo']
    search_fields = ['title']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['get_title', 'user_id', 'username', 'title', 'text', 'rating', ]
    list_display_links = ['get_title', ]
    readonly_fields = ['title', 'text']
    search_fields = ['title', 'text']

class UserAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_staff', 'is_superuser', 'id']
    # list_display_links = ['title', 'product_photo']
    # search_fields = ['title']

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(WishList, WishListAdmin)
admin.site.register(Review, ReviewAdmin)