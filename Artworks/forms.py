from django import forms
from .models import Artwork

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['title', 'medium', 'style', 'genre', 'year_created', 'image', 'description', 'price']
        widgets = {
            'medium': forms.Select(choices=Artwork.MEDIUM_CHOICES),
            'style': forms.Select(choices=Artwork.STYLE_CHOICES),
            'genre': forms.Select(choices=Artwork.GENRE_CHOICES),
        }
