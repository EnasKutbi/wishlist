from django import forms
from django.forms import ModelForm
from .models import Wish

class wishForm(ModelForm):
    class Meta:
        model = Wish
        fields = ('name', 'description', 'image', 'store')

