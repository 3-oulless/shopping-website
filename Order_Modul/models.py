from django.db import models
from Account_Modul.models import User
from Product.models import Product
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربر")
    is_paid = models.BooleanField(verbose_name="پرداخت شده/نشده",default=False)
    total_invoice = models.IntegerField(null=True,blank=True,verbose_name='جمع فاکتور')
    tracking_code = models.IntegerField(null=True,blank=True,verbose_name="کد رهگیری")
    address = models.TextField(null=True,blank=True,verbose_name="آدرس")
    postalـcode = models.CharField(max_length=20,null=True,blank=True,verbose_name="کد پستی")
    phone = models.CharField(max_length=20,null=True,blank=True,verbose_name='موبایل')
    payment_date = models.DateField(null=True,blank=True,verbose_name="تاریخ پرداخت")

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "لیست سبد خرید"

    def __str__(self):
        return str(self.user)
    

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,verbose_name="سبد خرید",related_name='order_detail')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="محصول")
    final_price = models.IntegerField(null=True,blank=True,verbose_name="قیمت نهایی")
    count = models.IntegerField(verbose_name="نعداد")

    class Meta:
        verbose_name = "جزییات محصول"
        verbose_name_plural = "لیست جزییات محصول"
    
    def __str__(self):
        return str(self.order)