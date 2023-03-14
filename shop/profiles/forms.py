from django import forms

from profiles.models import Profile


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=255)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())
    age = forms.IntegerField(min_value=18, required=False)
