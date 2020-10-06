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
    title       = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Enter the product name...",
            }))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "id": "product-desc",
                "placeholder": "Enter the product description...",
                "class": "style-class-name1 style-class-name2",
                "rows": 9,
                "columns": 70
                }))
    summary     = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "id": "product-summary",
                "placeholder": "Enter the product summary...",
                "class": "style-class-name1 style-class-name2",
                "rows": 9,
                "columns": 70
                }))
    price       = forms.DecimalField(initial=199.99)
    available   = forms.BooleanField(initial=True)