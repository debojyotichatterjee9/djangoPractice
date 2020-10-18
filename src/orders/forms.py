from django import forms

from .models import Order


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'order_code',
            'discount_elidgible',
            'discount_amount',
            'total_amount',
            'status'
        ]
    
    def clean_order_code(self):
        order_code = self.cleaned_data.get('order_code')
        if order_code.startswith('ORD-'):
            raise forms.ValidationError("Invalid Order Id")
        return order_code