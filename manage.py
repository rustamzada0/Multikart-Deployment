#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multikart.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# Shell Category
from product.models import *

# clothing=Category(title='Clothing', parent_id=None)
# clothing.save()

# bags=Category(title='Bags', parent_id=None)
# bags.save()

# footwear=Category(title='Footwear', parent_id=None)
# footwear.save()

# watchs=Category(title='Watches', parent_id=None)
# watchs.save()

# house=Category(title='House of Design', parent_id=None)
# house.save()

# beauty=Category(title='Beauty & Personal care', parent_id=None)
# beauty.save()

# home=Category(title='Home & Decor', parent_id=None)
# home.save()

# kitchen=Category(title='Kitchen', parent_id=None)
# kitchen.save()

# women=Category(title="Women's fashion", parent_id=clothing.id)
# women.save()

# men=Category(title="Men's fashion", parent_id=clothing.id)
# men.save()

# accessories=Category(title="Accessories", parent_id=clothing.id)
# accessories.save()

# dresses=Category(title="Dresses", parent_id=women.id)
# dresses.save()

# skirts=Category(title="Skirts", parent_id=women.id)
# skirts.save()

# westarn=Category(title="Westarn wear women", parent_id=women.id)
# westarn.save()

# ethic=Category(title="Ethic wear women", parent_id=women.id)
# ethic.save()

# sport=Category(title="Sport wear women", parent_id=women.id)
# sport.save()

# mensport=Category(title="Sport wear men", parent_id=men.id)
# mensport.save()

# menwestrn=Category(title="Westarn wear men", parent_id=men.id)
# menwestrn.save()

# menethic=Category(title="Ethic wear men", parent_id=men.id)
# menethic.save()

# fashion=Category(title="Fashion jewellery", parent_id=accessories.id)
# fashion.save()

# caps=Category(title="Caps and hats", parent_id=accessories.id)
# caps.save()

# precius=Category(title="Precious jawellery", parent_id=accessories.id)
# precius.save()

# necklaces=Category(title="Necklaces", parent_id=accessories.id)
# necklaces.save()

# earings=Category(title="Earings", parent_id=accessories.id)
# earings.save()

# wrist=Category(title="Wrist wear", parent_id=accessories.id)
# wrist.save()

# ties=Category(title="Ties", parent_id=accessories.id)
# ties.save()

# cufflinks=Category(title="Cufflinks", parent_id=accessories.id)
# cufflinks.save()

# pocket=Category(title="Pockets squares", parent_id=accessories.id)
# pocket.save()

# phone_cases=Category(title="Phone Cases", parent_id=accessories.id)
# phone_cases.save()

# shopper=Category(title="Shopper bags", parent_id=bags.id)
# shopper.save()

# laptop=Category(title="Laptop bags", parent_id=bags.id)
# laptop.save()

# cluthec=Category(title="Clutches", parent_id=bags.id)
# cluthec.save()

# purses=Category(title="All Purses", parent_id=bags.id)
# purses.save()

# subpurses=Category(title="Purses", parent_id=purses.id)
# subpurses.save()

# wallets=Category(title="Wallets", parent_id=purses.id)
# wallets.save()

# leathers=Category(title="Leathers", parent_id=purses.id)
# leathers.save()

# satchels=Category(title="Satchels", parent_id=purses.id)
# satchels.save()

# sportshoes=Category(title="Sport shoes", parent_id=footwear.id)
# sportshoes.save()

# formalshoes=Category(title="Formal shoes", parent_id=footwear.id)
# formalshoes.save()

# casualshoes=Category(title="Casual shoes", parent_id=footwear.id)
# casualshoes.save()

# makeup=Category(title="Makeup", parent_id=beauty.id)
# makeup.save()

# skincare=Category(title="Skincare", parent_id=beauty.id)
# skincare.save()

# premium=Category(title="Premium beauty", parent_id=beauty.id)
# premium.save()