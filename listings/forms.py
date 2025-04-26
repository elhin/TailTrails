from django import forms
from .models import Profile, PetPost

class PetPostForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['pet_ID', 'pet_name', 'species', 'age', 'desc', 'owner_contact', 'pet_image', 'created_date', 'published_date']

##from kayla
class PetPostForm(forms.ModelForm):
    class Meta:
        model = PetPost
        fields = [
            'status', 'pet_name', 'pet_type', 'breed', 'color', 'size',
            'last_seen_location', 'last_seen_date', 'contact_phone',
            'contact_email', 'description', 'photo'
        ]
        widgets = {
            'last_seen_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }