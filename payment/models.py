from django.db import models
from core.models import AbstractModel
from account.models import User
from product.models import Variant
# Create your models here.

class Cart(AbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    total_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    def title(self):
        return self.user.username

    def calculate_total_price(self):
        total_price = self.items.all().aggregate(models.Sum('total_price'))["total_price__sum"]
        self.total_price = total_price
        self.save()


class CartItem(AbstractModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    variant = models.ForeignKey(Variant,on_delete=models.CASCADE, related_name='cart')
    quantity = models.IntegerField()
    # size = models.ForeignKey('product.Size', on_delete=models.CASCADE, null=True, blank=True, related_name='sizes')
    size = models.CharField(max_length=10, null=True, blank=True)
    done = models.BooleanField(default=False)
    total_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.cart}---{self.variant}---{self.quantity}'
    
    def color(self):
        return self.variant.color

    def save(self, *args, **kwargs):
        self.total_price=round(float(self.variant.actual_price) * int(self.quantity),2)
        super(CartItem, self).save(*args, **kwargs)
        self.cart.calculate_total_price()

    # def save(self, *args, **kwargs):
    #         existing_item = CartItem.objects.filter(cart=self.cart, variant=self.variant, size=self.size).first()

    #         if existing_item:
    #             existing_item.quantity += self.quantity
    #             existing_item.total_price = round(float(existing_item.variant.actual_price) * int(existing_item.quantity), 2)
    #             existing_item.save()
    #             print('here')
    #         else:
    #             self.total_price = round(float(self.variant.actual_price) * int(self.quantity), 2)
    #             super(CartItem, self).save(*args, **kwargs)
    #             print('here 2')

    #         self.cart.calculate_total_price()


class Orders(AbstractModel):
    product=models.ForeignKey("product.Variant",on_delete=models.CASCADE, related_name='c')
    orderId=models.IntegerField(unique=False)
    quantity=models.IntegerField()
    first_name = models.CharField(max_length=50, null=True, blank=True, default='')
    last_name = models.CharField(max_length=50, null=True, blank=True, default='')
    email = models.CharField(max_length=50, null=True, blank=True, default='')      
    phone_number = models.CharField(max_length=50, null=True, blank=True, default='')
    flat = models.CharField(max_length=50, null=True, blank=True, default='')
    address = models.CharField(max_length=100, null=True, blank=True, default='')
    zip = models.CharField(max_length=50, null=True, blank=True, default='')
    country = models.CharField(max_length=50, null=True, blank=True, default='')
    city = models.CharField(max_length=50, null=True, blank=True, default='')
    region = models.CharField(max_length=50, null=True, blank=True, default='')
    payed = models.IntegerField()
    is_success = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product}---{self.orderId}---{self.first_name} {self.last_name}'