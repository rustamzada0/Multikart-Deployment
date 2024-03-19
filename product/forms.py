from django.forms import ModelForm
from django import forms
from account.models import Review        
        
class ReviewForm(ModelForm):

    class Meta:

        model = Review

        fields = ('title',
                  'text',
                'rating')

        widgets = {
           "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Title"
            }),

            "text": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Text"
            }),
        }