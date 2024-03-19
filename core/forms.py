from django.forms import ModelForm
from django import forms
from .models import Subscriber, Contact
from account.models import User, Subscriber

class SubscribeForm(ModelForm):
    
    class Meta:
        model = Subscriber

        fields = ['email']

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
            })
        }

    def clean(self):
        super().clean()
        if self.cleaned_data['email']:
            email = self.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                if Subscriber.objects.filter(email=email).exists():
                    self.errors['email'] = self.error_class([("This email address is already subscribed")])
            else:
                self.errors['email'] = self.error_class([("Please Sign Up First")])


class ContactForm(ModelForm):

    class Meta:
        model = Contact

        fields = (
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "message",
        )

        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "First Name"
            }),

            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Last Name"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email"
            }),

            "phone_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone Number",
            }),

            "message": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Message"
            }),

        }

    def clean(self):
        super().clean()
        if self.cleaned_data.get('first_name') == None:
            self.errors['first_name'] = self.error_class([('Empty first name!')])
        if self.cleaned_data.get('last_name') == None:
            self.errors['last_name'] = self.error_class([('Empty last name!')])
        if self.cleaned_data.get('email') == None:
            self.errors['email'] = self.error_class([('Empty email!')])
        if self.cleaned_data.get("phone_number") == None:
            self.errors['phone_number'] = self.error_class([('Empty Phone Number')])
        if self.cleaned_data.get('message') == None:
            self.errors['message'] = self.error_class([('Empty Message!')])