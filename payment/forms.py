from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name'}), required=True)
    shipping_phone = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}), required=True)
    shipping_address = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}), required=True)
    shipping_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), required=False)
    shipping_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}), required=False)

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name','shipping_phone','shipping_address','shipping_city','shipping_country']

        exclude = ['user',]


class PaymentForm(forms.Form):
    card_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Card Number', 'pattern':'[0-9]{16}', 'oninput': "setCustomValidity('')", 'oninvalid': "setCustomValidity('Please enter a 16-digit card number')"}), required=True)
    exp_month = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Expiration Month'}), required=True)
    exp_year = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Expiration Year'}), required=True)
    cvc = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'CVC'}), required=True)
