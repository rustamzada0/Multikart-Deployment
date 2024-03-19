from modeltranslation.translator import translator, TranslationOptions
from .models import *

class TranslationOptions(TranslationOptions):
    fields = ('title', 'text')

# translator.register(News, TranslationOptions)