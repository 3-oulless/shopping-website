from django.shortcuts import render
from django.views import View
from Site_Modul.models import Site_Setting,Social_Network_Site,Employee

class AboutUsView(View):
    def get(self,request):
        data_site = Site_Setting.objects.get(is_main_setting=True)
        social_network = Social_Network_Site.objects.filter(site_seting=data_site)
        employees = Employee.objects.filter(employee_alredy=True)

        context = {
            'data_site' : data_site,
            'social_network' : social_network,
            'employees' : employees,
        }
        return render(request,'about_us.html',context)