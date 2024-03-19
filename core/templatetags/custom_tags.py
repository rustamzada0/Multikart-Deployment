from django import template
from product.models import Category

register = template.Library()

@register.simple_tag
def Nav():
    categories = Category.objects.all()
    return categories