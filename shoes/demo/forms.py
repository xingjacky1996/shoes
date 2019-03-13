from django import forms
from .models import Shoes,User


class Userform(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'

class Shoesform(forms.ModelForm):
    class Meta:
        model=Shoes
        fields='__all__'