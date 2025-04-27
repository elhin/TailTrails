from django import forms
from .models import PetPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", 'email', 'password1', 'password2']
        