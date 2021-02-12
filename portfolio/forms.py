from django import forms
from .models import Visitor
from phonenumber_field.formfields import PhoneNumberField

class VisitorContactForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Full Name',
        }))

    phone_number = PhoneNumberField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Phone Number',
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email Address',
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Message',
        'rows': 7,
    }))

    class Meta:
        model = Visitor
        fields = '__all__'