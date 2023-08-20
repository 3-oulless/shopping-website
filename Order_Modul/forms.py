from django import forms

class PaymentForm(forms.Form):

    cart_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'شماره کارت را وارد کنید'}))
    cart_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'پسورد کارت را وارد کنید'}))