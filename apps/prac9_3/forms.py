from django import forms

class simpleForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()