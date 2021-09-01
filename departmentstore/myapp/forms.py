from django import forms
from django.forms import ModelForm
from . models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'order_quantity']
