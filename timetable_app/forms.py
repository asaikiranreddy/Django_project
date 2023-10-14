# timetable_app/forms.py
from django import forms
from .models import Subject
from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Import the User model

class RegistrationForm(UserCreationForm):
    # Your form fields and customization go here

    class Meta:
        model = User  # Use the User model
        fields = ['username', 'email', 'password1', 'password2']  # Example fields


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']
