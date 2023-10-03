from django import forms
from prac9_5.models import User

class createAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class loginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)