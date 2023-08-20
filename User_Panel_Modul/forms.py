from django import forms
from Account_Modul.models import User

class EditUserInformation(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar','first_name','last_name','about_user','address','postalـcode','phone','instagram_account','twitter_account','facbook_account','linkedin_account']

        labels = {
            'first_name' : 'نام',
            'last_name' : 'نام خانوادگی'
        }

        widgets = {
            'avatar' : forms.FileInput(attrs={"class" : "form-control" , "placeholder" : "لطفا عکس خود را وارد کنید"}),
            'first_name' : forms.TextInput(attrs={"class" : "form-control" , "placeholder" : "لطفا نام خود را وارد کنید"}),
            'last_name' : forms.TextInput(attrs={"class" : "form-control" , "placeholder" : "لطفا نام خانوادگی خود را وارد کنید"}),
            'about_user' : forms.Textarea(attrs={"class" : "form-control" , "placeholder" : "خود را معرفی کنید"}),
            'address' : forms.Textarea(attrs={"class" : "form-control" , "placeholder" : "آدرس خود را وارد کنید"}),
            'postalـcode' : forms.TextInput(attrs={"class" : "form-control" , "placeholder" : "کد پستی خود را وارد کنید"}),
            'phone' : forms.TextInput(attrs={"class" : "form-control" , "placeholder" : "شماره تماس خود را وارد کنید"}),
            'instagram_account' : forms.TextInput(attrs={"class" : "form-control" , "placeholder" : "لطفا آدرس اکانت اینستاگرام خود را وارد کنید"}),
            'twitter_account' : forms.TextInput(attrs={"class" : "form-control" , "placeholder" : "لطفا آدرس اکانت توییتر خود را وارد کنید"}),
            'facbook_account' : forms.TextInput(attrs={"class" : "form-control" , "placeholder" : "لطفا آدرس اکانت فیسبوک خود را وارد کنید"}),
            'linkedin_account' : forms.TextInput(attrs={"class" : "form-control" , "placeholder" : "لطفا آدرس اکانت لینکدین خود را وارد کنید"})

        }

class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'لطفا پسورد قدیمی خود را وارد کنید'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'لطفا پسورد خود را وارد کنید'}))
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'لطفا پسورد خود را نکرار کنید'}))

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password == re_password: 
            return password
        raise forms.ValidationError("Password Must Match")

