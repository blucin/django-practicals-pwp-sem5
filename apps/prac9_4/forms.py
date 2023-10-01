from django import forms
from prac9_4.models import fileFormSchema

class uploadFileForm(forms.ModelForm):
    class Meta:
        model = fileFormSchema
        fields = ['fileName', 'file']