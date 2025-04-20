from django import forms
from .models import Profile


class Imageform(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['pet_ID', 'pet_name', 'species', 'age', 'desc', 'owner_contact', 'pet_image', 'created_date', 'published_date']
