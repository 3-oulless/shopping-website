from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Product,ProductTag,ProductCategory,ProductBrand,ProductComment,ProductVisit,ProductGallery
from django.views.generic import ListView,TemplateView,DetailView,View
from django.core.paginator import Paginator
from modul.modul import get_client_ip,group_list
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin





@login_required()  
def Category_Filter(request,data):
    data = Product.objects.filter(category__url_title=data).order_by('-visit_count')
    brand = ProductBrand.objects.all()

    paginator = Paginator(data, 10)
    
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'product' : data,
        'page_obj' : page_obj,
        'paginator' : paginator,
        'brand' : brand,
    }

    return render(request,'Product/product_list.html',context)


@login_required()
def Brand_Filter(request,data):

    data = Product.objects.filter(brand__url_title=data).order_by('-visit_count')
    brand = ProductBrand.objects.all()

    paginator = Paginator(data, 10)
    
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'product' : data,
        'brand' : brand,
        'page_obj' : page_obj,
        'paginator' : paginator,
    }

    return render(request,'Product/product_list.html',context)


class ProductListView(ListView):
    model = Product
    template_name = 'Product/product_list.html'
    context_object_name = "product"
    ordering = ['-visit_count']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = ProductBrand.objects.all()
        context['brand'] = brand
        return context

class DetailView(LoginRequiredMixin,DetailView):
    model = Product
    template_name = "Product/product_detail.html"
    context_object_name = "data"

    def post(self,request,slug):
        data_pk = Product.objects.get(slug=slug)
        if request.user.is_authenticated:
            message = request.POST.get('message')
            user = request.POST.get('user')
            parent_id = request.POST.get('parentid')

            if parent_id is not "":
                ProductComment.objects.create(product_id=data_pk.pk,user_id=user,parent_id=parent_id,text=message)
                return redirect("products:example",slug=data_pk.slug)

            else:
                ProductComment.objects.create(product_id=data_pk.pk,user_id=user,text=message)

            return redirect("products:example",slug=data_pk.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = kwargs['object']

        #create visit count
        request = self.request
        user_ip = get_client_ip(request)
        user_id = None
        if request.user.is_authenticated:
            user_id = request.user
        has_been_visited = ProductVisit.objects.filter(ip__iexact=user_ip,product=product).first()
        if has_been_visited:
            p_data = Product.objects.get(id=has_been_visited.product.id)
            visit_count = ProductVisit.objects.filter(product=product).count()
            p_data.visit_count = visit_count
            p_data.save()
        else :
            ProductVisit.objects.create(ip=user_ip,user=user_id,product=product)
            

        #end visit count

        tag = ProductTag.objects.filter(product_tag=self.object)
        category = ProductCategory.objects.filter(id=product.id)
        context['comments'] = ProductComment.objects.filter(product__id=product.id,parent=None).order_by('-create_date').prefetch_related('product_parent')
        galleries = list(ProductGallery.objects.filter(product_id=product.id).all())
        galleries.insert(0,product)
        context['product_galleries_group'] = group_list(galleries,3)
        context['tag'] = tag
        context['category'] = category
        return context
    
