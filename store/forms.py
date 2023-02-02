from django import forms
from . models import Product_search

class Product_search_form(forms.ModelForm):
    name_of_produto = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control me-2", 'placeholder': 'Nome do produto', 'style': 'border-radius: 30px'
    }))
    class Meta:
        model = Product_search
        fields = ['name_of_produto',]