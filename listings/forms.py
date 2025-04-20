from django import forms
from .models import Profile


class Imageform(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['name', 'pet_image']
