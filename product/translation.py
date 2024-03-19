from modeltranslation.translator import translator, TranslationOptions
from .models import *

class VariantTranslationOptions(TranslationOptions):
    fields = ('title',)
    
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'desc', 'product_detail')

class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Product, ProductTranslationOptions)
translator.register(Variant, VariantTranslationOptions)
translator.register(Category, CategoryTranslationOptions)