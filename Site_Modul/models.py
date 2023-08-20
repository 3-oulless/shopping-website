import datetime
import os
import random
from django.db import models


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    BASE_LIST = '0123456789abcdefghijklmnopqrstuvwxyz'
    new_name = ''.join(random.choices(BASE_LIST, k=10))
    name,ext = get_filename_ext(filename)
    x = datetime.datetime.now()
    final_name = f"Banner/{x.year}/{x.month}/{x.day}/{new_name}{ext}"
    return f"Media/{final_name}"

class Site_Setting(models.Model):
    site_name = models.CharField(max_length=200,verbose_name="نام سایت")
    sitr_url = models.CharField(max_length=200,verbose_name="دامنه سایت")
    address = models.CharField(max_length=300,verbose_name="آدرس ")
    phone = models.CharField(max_length=200,null=True,blank=True,verbose_name="تلفن ")
    fax = models.CharField(max_length=200,null=True,blank=True,verbose_name="فکس ")
    email = models.CharField(max_length=200,null=True,blank=True,verbose_name="ایمیل ")
    copy_right = models.TextField(verbose_name="متن کپی رایت سایت")
    about_us_text = models.TextField(verbose_name="متن درباره سایت")
    site_logo = models.ImageField(upload_to='Site_Setting/',verbose_name="لوگو سابت")
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی')

    class Meta :
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "تنظیمات"
    
    def __str__(self):
        return self.site_name


class Employee(models.Model):
    employee_name = models.CharField(max_length=400,verbose_name="نام و نام خانوادگی کارمند")
    employee_image = models.ImageField(upload_to='Employees/',verbose_name="تصویر کارمند")
    employee_position = models.CharField(max_length=200,verbose_name="سِمَت کارمند")
    employee_alredy = models.BooleanField(default=True,verbose_name="آیا مشغول به کار است")
    employee_recruitment_date = models.DateTimeField(auto_now_add=True)

    class Meta :
        verbose_name = "کارمند شرکت"
        verbose_name_plural = "کارمندان"
    
    def __str__(self):
        return f'{self.employee_name}-{self.employee_position}'
    

class Social_Network_Site(models.Model):
    social_network_name = models.CharField(max_length=200,verbose_name="اسم سوشیال مدیا")
    social_network_url = models.CharField(max_length=200,verbose_name="لینک سوشیال مدیا")
    site_seting = models.ForeignKey(Site_Setting,on_delete=models.DO_NOTHING)

    class Meta :
        verbose_name = "اکانت فضای مجازی"
        verbose_name_plural = "اکانت های فضای مجازی"
    
    def __str__(self):
        return f'{self.site_seting.site_name} - {self.social_network_name}'


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200,verbose_name="عنوان")

    class Meta:
        verbose_name = "دسته بندی لینک های فوتر"
        verbose_name_plural = "دسته بندی های لینک های فوتر"

    def __str__(self):
        return self.title
    
class FooterLink(models.Model):
    title = models.CharField(max_length=200,verbose_name="عنوان")
    url = models.URLField(max_length=500,verbose_name="لینک")
    footer_link_box = models.ForeignKey(FooterLinkBox,on_delete=models.DO_NOTHING,verbose_name="دسته بندی",related_name="footer_link_box")

    class Meta:
        verbose_name = "لینک فوتر"
        verbose_name_plural = "لینک های فوتر"

    def __str__(self):
        return f'{self.footer_link_box.title} - {self.title}'
    



class Slider(models.Model):
    title = models.CharField(max_length=300,verbose_name="عنوان")
    url = models.CharField(max_length=300,verbose_name="لینک")
    url_title = models.CharField(max_length=400,verbose_name="عنوان لینک")
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to='Slider/',verbose_name="عکس")
    is_active = models.BooleanField(default=False,verbose_name="فعال با غیر فعال")

    class Meta :
        verbose_name = "اسلایدر"
        verbose_name_plural = "اسلایدر ها"
        
    def __str__(self):
        return self.title
    

class Site_Banner(models.Model):

    class Banner_Position(models.TextChoices):
        product_list = 'product_list','لیست محصولات',
        product_detail = 'product_detail','جزیات محصولات',
        contact_us = 'contact_us','ارتباط با ما',
    
    title = models.CharField(max_length=200,verbose_name="عنوان")
    url = models.URLField(max_length=400,null=True,blank=True,verbose_name="لینک تبلیغ")
    image = models.ImageField(upload_to=upload_image_path,verbose_name="تصویر تبلیغ")
    description = models.TextField(verbose_name="توضیحات",null=True,blank=True)
    is_active = models.BooleanField(verbose_name="فعال یا غیر فعال")
    position = models.CharField(max_length=200,choices=Banner_Position.choices)

    class Meta:
        verbose_name = "تلیغ"
        verbose_name_plural = "تبلیغات"

    def __str__(self):
        return self.title
