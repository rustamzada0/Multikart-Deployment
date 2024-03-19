from django.db import models
from django.db.models.fields import CharField, TextField, FloatField, SlugField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from core.models import AbstractModel
from django.utils.text import slugify
from django.utils import translation
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from account.models import Review

# Create your models here.

class Category(MPTTModel):
    title = CharField(max_length=50)
    image = ImageField(upload_to='category_media/', null=True, blank=True,)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='childs', on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    
    def __str__(self):
        if self.parent:
            categories = []
            categories.append(self.title)
            categories.append(self.parent.title)
            if self.parent.parent:
                most_parent = self.parent.parent
                categories.append(most_parent.title)
                while True:
                    if most_parent.parent:
                        most_parent = most_parent.parent
                        categories.append(most_parent.title)
                    else:
                        break
            title = f"{' ~ '.join(categories)}"
        else:
            title = self.title
        return title
    
    class Meta:
        verbose_name_plural = "Categories"
    
    class MPTTMeta:
        order_insertion_by = ['title']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.__str__())

        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        if self.parent:
            categories = []
            categories.append(self.slug)
            categories.append(self.parent.slug)
            if self.parent.parent:
                most_parent = self.parent.parent
                categories.append(most_parent.slug)
                while True:
                    if most_parent.parent:
                        most_parent = most_parent.parent
                        categories.append(most_parent.slug)
                    else:
                        break
            return f"{'/'.join(categories[::-1])}"
        else:
            return f'{self.slug}'


class Vendor(AbstractModel):
    name = CharField(max_length=50)
    image = ImageField(upload_to='vendor_media/')
    desc = TextField()
    # rating = DecimalField(max_digits=5, decimal_places=2)
    rating = FloatField(default=0.00)
    fb = CharField(max_length=50, null=True, blank=True)
    gp = CharField(max_length=50, null=True, blank=True)
    tw = CharField(max_length=50, null=True, blank=True)
    ig = CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Product(AbstractModel):
    title = CharField(max_length=100, unique=True)
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    general_stock = models.BooleanField(null=True, blank=True)
    product_detail = TextField(null=True, blank=True)
    desc = TextField(null=True, blank=True)
    video = CharField(max_length=100, null=True, blank=True)
    category = ForeignKey(Category, on_delete=models.CASCADE, related_name="related_product")
    vendor = ForeignKey('Vendor', on_delete=models.CASCADE)
    slug=models.SlugField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return f"{self.category.get_absolute_url()}/{self.slug}"

    def product_photo(self):
        variant = Variant.objects.filter(product = self).first()
        image = Image.objects.filter(variant = variant).filter(is_main=True).first()
        if image:
            return mark_safe('<img src="{}" width="100"/>'.format(image.image.url))


class Color(AbstractModel):
    title = CharField(max_length=35, unique=True)

    def __str__(self):
        return self.title


class Variant(AbstractModel):
    title = CharField(max_length=100, null=True, blank=True, unique=True)
    color = ForeignKey(Color, on_delete=models.CASCADE)
    product = ForeignKey(Product, on_delete=models.CASCADE, related_name="related_variants")
    new_status = models.BooleanField(default=False)
    discount_type=models.CharField(max_length=50, null=True, blank=True, choices=(('PRECENT' ,'Precent'), ('AMOUNT' , 'Amount')))
    discount_amount=models.IntegerField(null=True, blank=True)
    actual_price=models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    discount_time=models.DateTimeField(auto_now_add=False, null=True, blank=True)
    is_main_variant = models.BooleanField(default=False)
    is_main_image = ImageField(upload_to='product_media/', null=True, blank=True)
    slug = SlugField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=1)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.title = f"{self.product.title} {self.color.title}"

        self.slug = slugify(self.title)
        if self.discount_amount:
            if self.discount_type == 'PRECENT':
                self.actual_price=round(self.product.price-((self.product.price*self.discount_amount)/100),2)
            elif self.discount_type == 'AMOUNT':
                self.actual_price=round(self.product.price-self.discount_amount,2)        
        else: 
            self.actual_price=round(self.product.price,2)

        if self.is_main_variant:
                self.product.slug = self.slug
                self.product.save()

        super(Variant, self).save(*args, **kwargs)

    def variant_photo(self):
        image = Image.objects.filter(variant = self).filter(is_main=True).first()
        if image:
            return mark_safe('<img src="{}" width="100"/>'.format(image.image.url))

    def get_absolute_url(self):
        return f"{self.product.category.get_absolute_url()}/{self.slug}"
    
    def star(self):
        reviews = Review.objects.filter(variant=self)
        toti = 0
        period = 0
        for rev in reviews:
            toti += rev.rating
            period += 1
        if period == 0:
            period = 1
        result = round(toti / period)
        
        return result


class Image(AbstractModel):
    image = ImageField(upload_to='product_media/')
    is_main = models.BooleanField(default=False)
    variant = ForeignKey(Variant, on_delete=models.CASCADE, related_name="related_images")

    def __str__(self):
        return self.variant.title

    def title(self):
        return f"{self.variant.title}"
    
    def image_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))


class Size(AbstractModel):
    title = CharField(max_length=10, unique=True)

    def __str__(self):
        return self.title


class Option(AbstractModel):
    stock = models.IntegerField()
    size = ForeignKey(Size, on_delete=models.CASCADE)
    variant = ForeignKey(Variant , on_delete=models.CASCADE, related_name="related_option")

    class Meta:
        verbose_name_plural = "Options"
        verbose_name = "Option"
    
    def __str__(self):
        return f"{self.variant.title}"
    
    def option_photo(self):
        image = Image.objects.filter(variant=self.variant).filter(is_main=True).first()
        if image:
            return mark_safe('<img src="{}" width="100"/>'.format(image.image.url))