from django.forms import ModelForm
from django import forms
from .models import User, Profile


class RegisterForm(ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Confirm Password"
    }))

    class Meta:

        model = User

        fields = ("first_name", 
                  "last_name", 
                  "username", 
                  "email", 
                  "password",
                  "confirm_password")
        
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

            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Username",
            }),

            "password": forms.PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Password"
            }),

        }

    def clean(self):
        super().clean()
        if self.cleaned_data['first_name']:
            if not self.cleaned_data['first_name'].isalpha():
                self.errors['first_name'] = self.error_class([('Wrong first name')])
        else:
            self.errors['first_name'] = self.error_class([('Empty first name')])
        if self.cleaned_data['last_name']:
            if not self.cleaned_data['last_name'].isalpha():
                self.errors['last_name'] = self.error_class([('Wrong last name')])
        else:
            self.errors['last_name'] = self.error_class([('Empty last name')])
        if self.cleaned_data['email']:
            if User.objects.filter(email=self.cleaned_data['email']):
                self._errors['email']  = self.error_class([('This email already exists')])
        else:
            self.errors['email'] = self.error_class([('Empty email')])
        if self.cleaned_data.get("username") == None:
            self.errors['username'] = self.error_class([('Empty username')])
        else:
            if '@' in self.cleaned_data['username']:
                self._errors['username']  = self.error_class((['You cannot use @ in username']))
        if self.cleaned_data['password']:
            if len(self.cleaned_data['password']) < 8:
                self._errors['password'] = self.error_class([('Should Contain a minimum of 8 characters')])
            if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
                self._errors['confirm_password']  = self.error_class([('Not same password')])
        else:
            self.errors['password'] = self.error_class([('Empty Password!')])


class ProfileForm(ModelForm):

    class Meta:

        model = Profile

        fields = (
                    "first_name", 
                    "last_name", 
                    "phone_number", 
                    "email", 
                    "message",
                    "flat",
                    "address",
                    "zip",
                    "city",
                    "region",                  
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
                "placeholder": "Write Your Message"
            }),

            "flat": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Company Name"
            }),

            "address": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Address"
            }),

            "zip": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Zip Code"
            }),

            "city": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "City"
            }),

            "region": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Region / State"
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
            self.errors['phone_number'] = self.error_class([('Empty Phone Number!')])

        if self.cleaned_data.get('message') == None:
            print('salam')
            self.errors['message'] = self.error_class([('Empty Message!')])

        if self.cleaned_data.get('flat') == None:
            self.errors['flat'] = self.error_class([('Empty flat!')])

        if self.cleaned_data.get('address') == None:
            self.errors['address'] = self.error_class([('Empty address!')])

        if self.cleaned_data.get('zip') == None:
            self.errors['zip'] = self.error_class([('Empty zip!')])

        if self.cleaned_data.get('city') == None:
            self.errors['city'] = self.error_class([('Empty city!')])

        if self.cleaned_data.get('region') == None:
            self.errors['region'] = self.error_class([('Empty region!')])