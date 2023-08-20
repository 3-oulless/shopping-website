from typing import Any
from django import http
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views import View
from django.views.generic import ListView,DetailView
from Account_Modul.models import User
from .forms import EditUserInformation,ChangePasswordForm
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from Order_Modul.models import Order,OrderDetail



class UserPanelView(LoginRequiredMixin,TemplateView):

    def get(self, request):
        data = User.objects.get(id=request.user.id)
        context = {'data' : data}
        return render(request,'Panel/user_panel.html',context)

class EditUserInformationView(LoginRequiredMixin,View):

    def get(self,request):
        data = User.objects.filter(id=request.user.id).first()
        form_edit = EditUserInformation(initial={
            'first_name' : data.first_name,
            'last_name' : data.last_name,
            'about_user' : data.about_user,
            'address' : data.address,
            'postalـcode' : data.postalـcode,
            'phone' : data.phone,
            'instagram_account' : data.instagram_account,
            'twitter_account' : data.twitter_account,
            'facbook_account' : data.facbook_account,
            'linkedin_account' : data.linkedin_account
        },instance=data)

        context = {'form_edit' : form_edit}
        return render(request,'Panel/editprofile.html',context)

    def post(self,request):
        data = User.objects.filter(id=request.user.id).first()
        form_edit = EditUserInformation(request.POST, request.FILES,instance=data)
        if form_edit.is_valid():
            form_edit.save()
            return redirect('panel:user_panel')
        context = {'form_edit' : form_edit}
        return render(request,'Panel/editprofile.html',context)
        

class ChangePasswordView(LoginRequiredMixin,View):

    def get(self,request):
        form_data = ChangePasswordForm()
        context = {'form_data' : form_data}
        return render(request,'Panel/change_password.html',context)
    
    def post(self,request):
        form_data = ChangePasswordForm(request.POST or None)
        data = User.objects.filter(id=request.user.id).first()
        if form_data.is_valid():
            current_password = form_data.cleaned_data.get('current_password')
            password = form_data.cleaned_data.get('password')
            if data.check_password(current_password):
                data.set_password(password)
                data.save()
                logout(request)
                return redirect('account_modul:login')
            form_data.add_error('current_password','پسورد وارد شده اشتباه است')
        context = {'form_data' : form_data}
        return render(request,'Panel/change_password.html',context)


class OrdersView(LoginRequiredMixin,ListView):
    
    model = Order
    template_name = 'Panel/Orders.html'
    paginate_by = 10
    context_object_name = 'orders'

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        request = self.request
        queryset = queryset.filter(user_id=request.user.id,is_paid=True)
        return queryset
    
class OrderDetailView(LoginRequiredMixin,View):
    def get(self,request,pk):
        order = Order.objects.filter(id=pk,user_id=request.user.id).first()
        if order is None:
            return render(request,'404.html')
        orders = OrderDetail.objects.filter(order=order)
        context = {
            'orders' : orders
        }

        return render(request,'Panel/OrderDetail.html',context)



def componnent_list_group(request):
    return render(request,'Panel/componnent_list_group.html')