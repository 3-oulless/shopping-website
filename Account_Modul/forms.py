from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.Form):


    user_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'لطفا نام کاربری خود را وارد کنید'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'لطفا ایمیل خود را وارد کنید'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'لطفا پسورد خود را وارد کنید'}))
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'لطفا پسورد خود را نکرار کنید'}))

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password == re_password: 
            return password
        raise forms.ValidationError("Password Must Match")
    
    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        qs = User.objects.filter(username=user_name)
        if qs.exists():
            raise forms.ValidationError('Username is token')
        return user_name
    

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email is token')
        return email

    def clean_modile(self):
        modile = self.cleaned_data.get('modile')
        qs = User.objects.filter(modile=modile)
        if qs.exists():
            raise forms.ValidationError('Modile is token')
        return modile

class LoginForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'لطفا نام کاربری خود را وارد کنید'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'لطفا پسورد خود را وارد کنید'}))
    
class SendCodeForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'لطفا نام کاربری خود را وارد کنید'}))
    
class ChangePasswordForm(forms.Form):
    verify_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'لطفا کد تایید خود را وارد کنید'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'لطفا پسورد جدید خود را وارد کنید'}))