from django.shortcuts import render,redirect
from .forms import ContactUsForm
from django.views import View
from Site_Modul.models import Site_Setting,Social_Network_Site,Site_Banner
from django.contrib.auth.mixins import LoginRequiredMixin



class ContactUsView(LoginRequiredMixin,View):
    
    def get(self,request):
        form = ContactUsForm()
        data_site = Site_Setting.objects.get(is_main_setting=True)
        social_network = Social_Network_Site.objects.filter(site_seting=data_site)
        banner = Site_Banner.objects.filter(is_active = True,position__iexact = Site_Banner.Banner_Position.contact_us )
        context = {
            'form':form,
            'data_site' : data_site,
            'social_network' : social_network,
            'banners' : banner,
            }
        return render(request,'contact_us.html',context)

    def post(self,request):
        form = ContactUsForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
