from django import forms
from .models import CropImage

class CropImageForm(forms.ModelForm):
    class Meta:
        model = CropImage
        fields = ['image']
