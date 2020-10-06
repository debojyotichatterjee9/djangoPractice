from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
        'title',
        'description',
        'price',
        'summary',
        'available',
    ]
        
        
class RawProductForm(forms.Form):
    title       = forms.CharField()
    description = forms.CharField()
    summary     = forms.CharField()
    price       = forms.DecimalField()
    available   = forms.BooleanField()