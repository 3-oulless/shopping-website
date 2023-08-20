from django.http import Http404
from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterForm,LoginForm,SendCodeForm,ChangePasswordForm
from .models import User,Verify_Code
from django.utils.crypto import get_random_string
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth import get_user_model
import random


def randome_digit():
    return random.randrange(1111,9999)


user_module = get_user_model()


class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        context = {'form':register_form}
        return render(request,'Account/register.html',context)  
      
    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            
            
            username = register_form.cleaned_data.get('user_name')
            email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password')

            new_user = User(username=username,email=email,email_active_code=get_random_string(72),is_active=False)
            new_user.set_password(password)
            new_user.save()

            return redirect('account_modul:login')
        return render(request,'Account/register.html',context={'form':register_form})


class LoginView(View):
    def get(self,request):
        register_form = LoginForm()
        context = {'form':register_form}
        return render(request,'Account/login.html',context)  
      
    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
    
            username = login_form.cleaned_data.get('user_name')
            password = login_form.cleaned_data.get('password')

            User = authenticate(request,username=username,password=password)

            if User is not None:
                login(request,User)
                return redirect('/')
            else:
                if user_module.objects.filter(username=username):
                    login_form.add_error("password"," کلمه ی عبور اشتباه است")
                else:
                    login_form.add_error("user_name"," نام کاربری اشتباه است")


        if request.user.is_authenticated :
            return redirect('/')
        return render(request,'Account/login.html',context={'form':login_form})

class LogotView(View):
    def get(self,request):
        logout(request)
        return redirect('/')

class ActivateAccountView(View):
    def get(self,request,email_active_code):
        active_user = user_module.objects.filter(email_active_code__iexact=email_active_code).first()
        if active_user is not None:
            if not active_user.is_active:
                active_user.is_active = True
                active_user.email_active_code = get_random_string(72)
                active_user.save()
                return redirect('account_modul:login')
            else:
                pass
                #show message you are activated
        raise Http404

class Send_Code(View):
    def get(self,request):
        form = SendCodeForm()
        context = {'form' : form}
        return render (request,'Reset_Password/verify.html',context)

    def post(self,request):
        form = SendCodeForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('user_name')
            user_filter_by_useranme = User.objects.filter(username=username).first()
            if user_filter_by_useranme is not None:
                #send code by email for user
                Verify_Code.objects.create(user=user_filter_by_useranme,code=randome_digit())
                return redirect('account_modul:change_password')
            form.add_error('user_name','نام کاربری وجود ندارد')
            context = {'form' : form}
            return render (request,'Reset_Password/verify.html',context)

class Chanch_Password(View):
    def get(self,request):
        form = ChangePasswordForm()
        context = {'form' : form}
        return render(request,'Reset_Password/change_password.html',context)

    def post(self,request):
        form = ChangePasswordForm(request.POST or None)
        context = {'form' : form}
        if form.is_valid():
            verify_code = form.cleaned_data.get('verify_code')
            password = form.cleaned_data.get('password')

            try:
                data = Verify_Code.objects.get(code__iexact=int(verify_code))
                print(data)
                data_now = User.objects.get(username=data.user.username)
                print(data_now.username)
                data_now.set_password(password)
                data_now.save()
                data.delete()
                return redirect('account_modul:login')
            except:
                form.add_error('verify_code',"کد وارد شده صحیح نمیباشد")
            return render(request,'Reset_Password/change_password.html',context)

