from django import forms
from .models import Elon

class ElonForm(forms.ModelForm):
    class Meta:
        model = Elon
        fields = ['title', 'price', 'description', 'image','category']
