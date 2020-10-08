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
            "class": "form-control",
            "size": "20"
            }))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "id": "product-desc",
                "placeholder": "Enter the product description...",
                "class": "form-control",
                "rows": 9,
                "columns": 70
                }))
    summary     = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "id": "product-summary",
                "placeholder": "Enter the product summary...",
                "class": "form-control",
                "rows": 9,
                "columns": 70
                }))
    price       = forms.DecimalField(initial=199.99, widget=forms.TextInput(
            attrs={
                "placeholder": "Enter the product price...",
                "type": "number",
                "class": "form-control",
                "size": "20"
                }))
    available   = forms.BooleanField(initial=True, widget=forms.CheckboxInput(
            attrs={
                "class": ""
                }))
    
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not title.startswith("PRD-"):
            raise forms.ValidationError("Invalid product name!")
        return title
            