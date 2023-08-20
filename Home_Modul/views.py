from django.shortcuts import render
from Product.models import ProductBrand,ProductCategory
from django.views.generic import TemplateView
from Site_Modul.models import Site_Setting,FooterLinkBox,Slider,Social_Network_Site
from django.db.models import Count
# Create your views here.


class HomeView (TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        slider = Slider.objects.filter(is_active=True)
        context['slider'] = slider
        return context

def sit_header_component(request,*args,**kwargs):
    site_data = Site_Setting.objects.get(is_main_setting=True)
    Social_Network = Social_Network_Site.objects.filter(site_seting=site_data.id)
    category = ProductCategory.objects.filter(is_active=True,parent_id=None)
    context = {
        'data' : site_data,
        'product_categorys' : category,
        'social_network' : Social_Network
        }
    return render(request,'shared/Header.html',context)

def sit_footer_component(request,*args,**kwargs):
    site_data = Site_Setting.objects.get(is_main_setting=True)
    footer_link_box = FooterLinkBox.objects.all()
    context = {
        'site_data' : site_data,
        'footer_link_box' : footer_link_box
        }
    return render(request,'shared/Footer.html',context)

def grouping(request):
    brand = ProductBrand.objects.annotate(product_count=Count('product')).filter(is_active=True)
    category = ProductCategory.objects.filter(is_active=True,parent_id=None)
    context = {
        'brand' : brand,
        'product_categorys' : category,
    }
    return render(request,'shared/grouping.html',context)
