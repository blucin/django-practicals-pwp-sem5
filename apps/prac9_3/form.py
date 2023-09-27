from django import forms

class FormDataForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()