from django import forms
from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta :
        model = ContactUs
        fields = ["full_name",'email','title','message']

        widgets = {
            'full_name' : forms.TextInput(attrs={"class" : "form-control" , "placeholder" : "نام و نام خانوادگی"}),
            'email' : forms.EmailInput(attrs={"class" : "form-control" , "placeholder" : "ایمیل"}),
            'title' : forms.TextInput(attrs={"class" : "form-control" , "placeholder" : "عنوان"}),
            'message' : forms.Textarea(attrs={"class" : "form-control" ,"rows" : "8","id" : "message", "placeholder" : "متن پیام"})
        }
    

 