from django import forms
from .models import Product, 


class OrderForm(forms.ModelForm):

    class Meta:
        model = 
        fields = ['name', 'order_quantity']