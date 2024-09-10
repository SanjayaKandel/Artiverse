from django import forms
from .models import Artwork, Exhibition

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['title', 'medium', 'style', 'genre', 'year_created', 'image', 'description', 'price']
        widgets = {
            'medium': forms.Select(choices=Artwork.MEDIUM_CHOICES),
            'style': forms.Select(choices=Artwork.STYLE_CHOICES),
            'genre': forms.Select(choices=Artwork.GENRE_CHOICES),
        }
class DateInput(forms.DateInput):
    input_type = 'date'
    
class ExhibitionForm(forms.ModelForm):
    class Meta:
        model = Exhibition
        fields = ['title', 'start_date', 'end_date', 'description', 'brief_description', 'thumbnail']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }
