from django import forms
from .models import Exhibition

class DateInput(forms.DateInput):
    input_type = 'date'
    
class ExhibitionForm(forms.ModelForm):
    class Meta:
        model = Exhibition
        fields = ['title', 'start_date', 'end_date', 'curator', 'description', 'brief_description', 'thumbnail']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }
