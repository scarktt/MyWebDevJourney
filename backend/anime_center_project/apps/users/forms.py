from django import forms
from . models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
