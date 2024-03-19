from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.files import ImageField
from django.utils import timezone

# Create your models here.

class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super(AbstractModel, self).save(*args, **kwargs)


class Creator(AbstractModel):
    full_name = CharField(max_length=50)
    speciality = CharField(max_length=50)
    desc = TextField(blank=True)
    image = ImageField(upload_to='core_media/')


class About(AbstractModel):
    desc = TextField()
    address = TextField()
    email = CharField(max_length=50)
    phone_number = CharField(max_length=50)
    fax = CharField(max_length=50)
    image = ImageField(upload_to='main_media/')


class Faq(AbstractModel):
    answer = TextField()
    question = TextField()


class Contact(AbstractModel):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    phone_number = CharField(max_length=50)
    email = CharField(max_length=50)
    message = TextField()


class Subscriber(AbstractModel):
    email = CharField(max_length=50)

    def __str__(self) -> str:
        return self.email


class MainPhotos(AbstractModel):
    title = CharField(max_length=255, null=True, blank=True)
    creator = CharField(max_length=50, null=True, blank=True)
    date = CharField(max_length=50, null=True, blank=True)
    image = ImageField(upload_to='main_media/')
    blog = models.BooleanField(default=False)
    insta = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "MainPhotos"
        verbose_name = "MainPhotos"