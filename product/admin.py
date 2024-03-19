from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from modeltranslation.admin import TranslationAdmin
from .models import *


# Register your models here.

class VariantInline(admin.TabularInline):
    model = Variant
    extra = 1
    fields = ('color', 'is_main_variant', 'is_main_image')


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class OptionInline(admin.TabularInline):
    model = Option
    extra = 1


class ProductsAdmin(TranslationAdmin):
    list_display = ('title', 'category', 'vendor', 'product_photo')
    list_display_links = ['title', 'product_photo']
    search_fields = ['title']
    inlines = [
        VariantInline,
    ]


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_photo', 'is_main')
    list_display_links = ['title', 'image_photo']


class OptionsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'stock', 'option_photo')
    list_display_links = ['__str__', 'option_photo']


# class ChannelAdmin(admin.TabularInline):
#     model = Image
#     extra = 1
#     show_change_link = True


class VariantsAdmin(TranslationAdmin):
    list_display = ('title', 'variant_photo')
    list_display_links = ['title', 'variant_photo']
    inlines = [
        ImageInline, OptionInline
    ]



# class Categories(admin.ModelAdmin):
#     list_display = ['title']
#     list_display_links = ['title']
#     search_fields = ['title']


class CategoryAdmin(TranslationAdmin, DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Product, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Variant, VariantsAdmin)
admin.site.register(Option, OptionsAdmin)
admin.site.register(Image, ImageAdmin)