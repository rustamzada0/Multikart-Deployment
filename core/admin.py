from django.contrib import admin
from .models import *

# Register your models here.

class MainPhotosAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ['title',]


admin.site.register(About)
admin.site.register(Creator)
admin.site.register(Faq)
admin.site.register(Contact)
admin.site.register(Subscriber)
admin.site.register(MainPhotos, MainPhotosAdmin)