# forms.py
from django import forms
from .models import AdminProfile

class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = AdminProfile
        fields = [
            'profile_picture','name', 'biography', 'post', 'phone_number', 
            'address', 'city', 'country', 'department', 
            'linkedin', 'github'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Full Name',
                'class': 'placeholder'
            }),
            'biography': forms.Textarea(attrs={
                'placeholder': 'Hi i am ....',
                'class': 'placeholder'
            }),
            'post': forms.TextInput(attrs={
                'placeholder': 'Eg: Frontend developer',
                'class': 'placeholder'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Eg: 98xxxxxxxx',
                'class': 'placeholder'
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Eg: Kalika marga',
                'class': 'placeholder'
            }),
            'city': forms.TextInput(attrs={
                'placeholder': 'Eg: Kathmandu',
                'class': 'placeholder'
            }),
            'country': forms.TextInput(attrs={
                'placeholder': 'Eg: Nepal',
                'class': 'placeholder'
            }),
            'department': forms.TextInput(attrs={
                'placeholder': 'Eg: IT Department',
                'class': 'placeholder'
            }),
            'linkedin': forms.TextInput(attrs={
                'placeholder': 'Eg: LinkedIn profile',
                'class': 'placeholder'
            }),
            'github': forms.TextInput(attrs={
                'placeholder': 'GitHub profile',
                'class': 'placeholder'
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'profile-picture-input'
            }),
        }
