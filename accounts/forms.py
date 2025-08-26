# forms.py in your accounts app

from django import forms
from django.contrib.auth import authenticate

from .models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        foo = User.objects.filter(username=username)
        if foo.exists():
            raise forms.ValidationError('username already exists')
        return username

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Passwords do not match')
        return data

    def save(self, commit=True):
        # Save the Employee instance first
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')

        if password:
            user.set_password(password)  # This is the crucial line for hashing the password!

        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   "placeholder": "username"}))

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   "placeholder": "password"}))



    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username or password")
            cleaned_data["user"] = user
        return cleaned_data