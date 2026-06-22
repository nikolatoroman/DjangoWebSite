from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password1(self):
        password = self.cleaned_data.get('password1')

        if len(password) < 8:
            raise forms.ValidationError("Password must have at least 8 characters.")

        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError("Password must contain at least one capital letter.")

        if not re.search(r'\d', password):
            raise forms.ValidationError("Password must contain at least one number.")

        return password