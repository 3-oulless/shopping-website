from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import Order,OrderDetail
from Product.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
import random
from .forms import PaymentForm
import datetime

def tracking_code():
    digit = random.randrange(000000000000,999999999999)
    return digit


@login_required()
def add_product_to_order(request):
    product_id = int(request.GET.get('product_id'))
    count = int(request.GET.get('count'))

    if count < 1:
        return JsonResponse({
            'status' : 'invalid_count',
            'title': 'اعلان',
            'text': "تعداد مشخص شده نامعتبر است",
            'icon': 'error',
            'confirmButtonColor': '#3085d6',
            'confirmButtonText': 'باشه ممنون'
            

            })

    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id,is_active=True,is_delete=False).first()
        if product is not None:
            current_order,create = Order.objects.get_or_create(is_paid=False,user_id=request.user.id)
            current_order_detail = current_order.order_detail.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += count
                current_order_detail.save()
            else:
                OrderDetail.objects.create(order_id=current_order.id,product_id=product_id,count=count)
            return JsonResponse({
                'status' : 'success',
                'title': 'اعلان',
                'text': "محصول شما با موفقیت به سبد خرید اضافه شد",
                'icon': 'success',
                'confirmButtonText': 'باشه ممنون'
            })
        else:
            
            return JsonResponse({
                'status' : 'not_found',
                'title': 'اعلان',
                'text': "محصول مورد نیاز پیدا نشد",
                'icon': 'error',
                'confirmButtonColor': '#3085d6',
                'confirmButtonText': 'باشه ممنون'
            })
    else:
        return JsonResponse({
            'status' : 'not_auth',
            'title': 'اعلان',
            'text': "لطفا ابتدا وارد حساب کاربری خود شوید",
            'icon': 'error',
            'confirmButtonColor': '#3085d6',
            'confirmButtonText': 'باشه ممنون'
            })


@login_required()
def show_order(request):

    order = Order.objects.filter(user_id=request.user.id,is_paid=False).first()

    order_detail = OrderDetail.objects.filter(order=order)

    for order_final_price in order_detail:
        order_final_price.final_price = order_final_price.count * order_final_price.product.price
        order_final_price.save()

    final_price = 0
    for sum_all_price in order_detail:
        final_price = sum_all_price.final_price + int(final_price)

    order_id = request.GET.get('order_id')

    order_detail_remove = OrderDetail.objects.filter(pk=order_id,order__user_id=request.user.id,order__is_paid=False).first()
   


    if order_detail_remove:
        order_detail_remove.delete()
        return JsonResponse({
                'status' : 'success',
                'title': 'اعلان',
                'text': "محصول شما با موفقیت حذف شد",
                'icon': 'success',
                'confirmButtonText': 'باشه ممنون'
            })




    context = {
        'order':order,
        'final_price':final_price,
        }
    return render(request,'Order/order.html',context)


class FinalStepOrder(LoginRequiredMixin,View):

    

    def get(self,request):
        order_data = Order.objects.get(user_id=request.user.id,is_paid=False)
        form = PaymentForm()
        context = {
            'form':form,
            'order_data' : order_data
        }
        return render(request,'Order/by_html.html',context)
    
    def post(self,request):

        form = PaymentForm(request.POST or None)
        order_data = Order.objects.get(user_id=request.user.id,is_paid=False)

        context = {
            'form':form,
            
        }

        if form.is_valid():
            trackingcode = tracking_code()
            
            order_detail = OrderDetail.objects.filter(order=order_data)

            final_price = 0
            for sum_all_price in order_detail:
                final_price = sum_all_price.final_price + final_price

            order_data.total_invoice = final_price
            order_data.tracking_code = trackingcode
            order_data.address = request.user.address
            order_data.postalـcode = request.user.postalـcode
            order_data.phone = request.user.phone
            order_data.payment_date = datetime.date.today()
            order_data.is_paid = True
            order_data.save()

            return redirect('order:ShowPaymentInformation',pk=order_data.pk , id=request.user.id)

        return render(request,'Order/by_html.html',context)

class ShowPaymentInformation(View):

    def get(self,request,pk,id):
        order_data = Order.objects.get(pk=pk,user_id=id)
        context = {
            'order' : order_data
        }

        return render (request,'Order/ShowPaymentInformation.html',context)

        

