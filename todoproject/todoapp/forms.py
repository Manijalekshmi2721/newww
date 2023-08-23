from django import forms
from .models import Todoclass

class form1(forms.ModelForm):
    class Meta:
        model=Todoclass
        fields=['name','priority','date']
