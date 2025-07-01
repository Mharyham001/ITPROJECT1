from django import forms
from .models import Product 


class OrderForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity']