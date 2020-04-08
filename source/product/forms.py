from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    #this overrides the title field that was already declared below
    title       = forms.CharField(label='',
                                    widget=forms.TextInput(
                                        attrs={
                                            "placeholder": "Enter the title here..."
                                        }))
    description = forms.CharField(required=False,
                                    widget=forms.Textarea(
                                        attrs={
                                            "placeholder": "Enter the description here...",
                                            "class": "new-class-name1 new-class-name2",
                                            "id": "my-product-description",
                                            "rows": 2,
                                            "columns": 10
                                        }))
    price       = forms.DecimalField(initial=199.99)
    summary     = forms.CharField(required=False,
                                    widget=forms.Textarea(
                                    attrs={
                                        "placeholder": "Enter the summary here...",
                                        "class": "new-class-name1 new-class-name2",
                                        "id": "my-product-summary",
                                        "rows": 2,
                                        "columns": 10
                                    }))
    featured    = forms.BooleanField()
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary',
            'featured'
        ]
        # doing filed validation here below...
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "PRD-" in title:
            raise forms.ValidationError("This is not a valid Title format!!! Please put 'PRD-' before the title name.")
        return title


class RawProductForm(forms.Form):
    title       = forms.CharField(label='',
                                    widget=forms.TextInput(
                                        attrs={
                                            "placeholder": "Enter the title here..."
                                        }))
    description = forms.CharField(required=False,
                                    widget=forms.Textarea(
                                        attrs={
                                            "placeholder": "Enter the description here...",
                                            "class": "new-class-name1 new-class-name2",
                                            "id": "my-product-description",
                                            "rows": 2,
                                            "columns": 10
                                        }))
    price       = forms.DecimalField(initial=199.99)
    summary     = forms.CharField(required=False,
                                    widget=forms.Textarea(
                                    attrs={
                                        "placeholder": "Enter the summary here...",
                                        "class": "new-class-name1 new-class-name2",
                                        "id": "my-product-summary",
                                        "rows": 2,
                                        "columns": 10
                                    }))
    featured    = forms.BooleanField()
