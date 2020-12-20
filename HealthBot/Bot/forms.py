from django import forms
from django.contrib.auth.models import User




# Overiding the Model form with 3 fields 

class RegisterationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email','password']



