from django.db import models
from django.db.models.fields import CharField, TextField, FloatField, BooleanField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import AbstractUser
from core.models import AbstractModel
from django.contrib.auth.models import User
from django.db.models.signals import post_save 
from django.utils.text import slugify
from core.models import *
from product.models import *


# Create your models here.


class User(AbstractUser):
    first_name = CharField(max_length=50, null=True, blank=True, default='')
    last_name = CharField(max_length=50, null=True, blank=True, default='')
    password = CharField(max_length=255, null=True, blank=True, default='')
    email = CharField(max_length=50, unique=True, null=True, blank=True, default='')
    phone_number = CharField(max_length=50, null=True, blank=True, default='')
    flat = CharField(max_length=50, null=True, blank=True, default='')
    address = CharField(max_length=100, null=True, blank=True, default='')
    zip_code = CharField(max_length=50, null=True, blank=True, default='')
    country = CharField(max_length=50, null=True, blank=True, default='')
    city = CharField(max_length=50, null=True, blank=True, default='')
    region = CharField(max_length=50, null=True, blank=True, default='')
    card = CharField(max_length=16, null=True, blank=True, default='')
    forget_pwd_token = CharField(max_length=100,null=True,blank=True)
    email_confirmed = BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True, editable=False)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.username
    
    # def save(self, *args, **kwargs):
    #     if not self.created_at:
    #         self.created_at = timezone.now()
    #     self.updated_at = timezone.now()
    #     super(User, self).save(*args, **kwargs)


class WishList(AbstractModel):
    user = ForeignKey(User, on_delete=models.CASCADE)
    variant = ForeignKey("product.Variant", on_delete=models.CASCADE)

    def title(self):
        return self.variant.title
    
    def username(self):
        return self.user.get_full_name()
    
    def user_id(self):
        return self.user.id
    
    def product_photo(self):
        image = Image.objects.filter(variant = self.variant).filter(is_main=True).first()
        if image:
            return mark_safe('<img src="{}" width="100"/>'.format(image.image.url))


class Review(AbstractModel):
    rates = {
        (1, "⭐"),
        (2, "⭐⭐"),
        (3, "⭐⭐⭐"),
        (4, "⭐⭐⭐⭐"),
        (5, "⭐⭐⭐⭐⭐")
    }

    user = ForeignKey(User, on_delete=models.CASCADE)
    variant = ForeignKey("product.Variant", on_delete=models.CASCADE, related_name='vvv')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(null=True, blank=True, choices=rates)

    def get_title(self):
        return self.variant.title
    
    def username(self):
        return self.user.get_full_name()
    
    def user_id(self):
        return self.user.id
    
    # def product_photo(self):
    #     image = Image.objects.filter(variant = self.variant).filter(is_main=True).first()
    #     if image:
    #         return mark_safe('<img src="{}" width="100"/>'.format(image.image.url))
    
    # def save(self, *args, **kwargs):
    #     reviews = Review.objects.filter(variant=self.variant)
    #     toti = 0
    #     period = 0
    #     for rev in reviews:
    #         toti += rev.rating
    #         period += 1
    #     if period == 0:
    #         period = 1
    #     print(int(toti / period))
    #     self.variant.rating = int(toti / period)
    #     print(self.variant.rating)
    #     return super().save(*args, **kwargs)
        

class Profile(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True, default='')
    last_name = models.CharField(max_length=50, null=True, blank=True, default='')
    phone_number = models.CharField(max_length=50, null=True, blank=True, default='')
    email = CharField(max_length=50, null=True, blank=True, default='')
    message = models.TextField(null=True, blank=True, default='')
    flat = models.CharField(max_length=50, null=True, blank=True, default='')
    address = models.CharField(max_length=100, null=True, blank=True, default='')
    zip = models.CharField(max_length=50, null=True, blank=True, default='')
    country = models.CharField(max_length=50, null=True, blank=True, default='')
    city = models.CharField(max_length=50, null=True, blank=True, default='')
    region = models.CharField(max_length=50, null=True, blank=True, default='')
    card = models.CharField(max_length=16, null=True, blank=True, default='')
    forget_pwd_token = models.CharField(max_length=100,null=True,blank=True)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        self.user = User.objects.filter(email = self.email).first()

        return super().save(*args, **kwargs)

    # def create_profile(sender, **kwargs):
    #     if kwargs['created']:
    #         user_profile = Profile.objects.create(user=kwargs['instance'])

    # post_save.connect(create_profile, sender=User)