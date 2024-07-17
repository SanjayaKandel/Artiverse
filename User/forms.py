from django import forms
from .models import Visitor
from .models import BillingAddress

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name', 'biography', 'profile_picture','gender', 'contact_phone', 'birth_date' ,'occupation']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
     

class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['address', 'city', 'state', 'country', 'zip_code']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
        }
