import datetime
import os
import random
from django.db import models
from Account_Modul.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    BASE_LIST = '0123456789abcdefghijklmnopqrstuvwxyz'
    new_name = ''.join(random.choices(BASE_LIST, k=10))
    name,ext = get_filename_ext(filename)
    x = datetime.datetime.now()
    final_name = f"Products/{x.year}/{x.month}/{x.day}/{new_name}{ext}"
    return f"Media/{final_name}"

def upload_image_path_gallery(instance,filename):
    BASE_LIST = '0123456789abcdefghijklmnopqrstuvwxyz'
    new_name = ''.join(random.choices(BASE_LIST, k=10))
    name,ext = get_filename_ext(filename)
    x = datetime.datetime.now()
    final_name = f"Gallery/{x.year}/{x.month}/{x.day}/{new_name}{ext}"
    return f"Media/{final_name}"

class ProductCategory(models.Model):
    parent = models.ForeignKey('ProductCategory',on_delete=models.CASCADE,null=True,blank=True,verbose_name="دسته بندی والد",related_name="parents")
    title_fa = models.CharField(max_length=100,db_index=True,verbose_name="عنوان")
    url_title = models.CharField(max_length=100,db_index=True,verbose_name="عنوان در url")
    is_active = models.BooleanField(verbose_name="فعال/غیر فعال")
    is_delete = models.BooleanField(verbose_name="حذف شده/نشده")


    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def get_absolute_url(self):
        return reverse('product:category_filter',args=[self.url_title])

    def __str__(self):
        return self.title_fa
    

class ProductBrand(models.Model):
    title = models.CharField(max_length=300,db_index=True,verbose_name="نام برند")
    url_title = models.CharField(max_length=300,db_index=True,verbose_name="نام برند در url",null=True)
    is_active = models.BooleanField(verbose_name="فعال/غیر فعال")

    def get_absolute_url(self):
        return reverse('product:brand_filter',args=[self.url_title])

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'
    
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=300,verbose_name="عنوان")
    brand = models.ForeignKey(ProductBrand,on_delete=models.CASCADE,verbose_name="برند شرکت",null=True)
    category = models.ManyToManyField(ProductCategory,related_name='product_category',verbose_name="دسته بندی ها")
    price = models.IntegerField(verbose_name="قیمت")
    short_description = models.CharField(max_length=360,db_index=True,verbose_name="توضیحات کوتاه")
    description = models.TextField(verbose_name="توضیحات اصلی",db_index=True)
    count = models.IntegerField(verbose_name="تعداد",null=True)
    image = models.ImageField(upload_to=upload_image_path,null=True,verbose_name="تصویر کالا")
    slug = models.SlugField(unique=True,default='',db_index=True,max_length=200,verbose_name="عنوان در url",null=True,blank=True)
    is_active = models.BooleanField(verbose_name="فعال/غیر فعال")
    is_delete = models.BooleanField(verbose_name="حذف شده/نشده")
    visit_count = models.IntegerField(null=True,blank=True,default=0,verbose_name='نعداد بازدید')

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def get_absolute_url(self):
        return reverse('product:example',args=[self.slug])

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return f'{self.id} - {self.title}'
    

class ProductTag(models.Model):
    caption = models.CharField(max_length=100,db_index=True,verbose_name="عنوان")
    product_tag = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_tags",verbose_name="نگ ها")

    class Meta:
        verbose_name = "تگ محصول"
        verbose_name_plural = "تگ های محصولات"

    def get_absolute_url(self):
        return reverse('product:tag_filter',args=[self.url_tag])

    def __str__(self):
        return self.caption


class ProductComment(models.Model):
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING,verbose_name="محصول")
    parent = models.ForeignKey('ProductComment',null=True,blank=True,on_delete=models.DO_NOTHING,verbose_name="والد",related_name="product_parent")
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name="کاربر")
    create_date = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ثبت")
    text = models.TextField(verbose_name="متن نظر")
    inspection = models.BooleanField(default=True,verbose_name="بازرسی")

    class Meta:
        verbose_name = "نظر محصول"
        verbose_name_plural = "نظرات محصولات"
    
    def __str__(self):
        return f'{self.product.title} - {self.create_date} - {self.id}'


class ProductVisit(models.Model):
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING,verbose_name="نام محصول")
    ip = models.CharField(max_length=30,verbose_name='آپی کاربر')
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True,verbose_name="کاربر")

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدید محصولات' 

    
    def __str__(self):
        return f'{self.product.title}-{self.ip}'
    

class ProductGallery(models.Model):
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING,verbose_name='محصول')
    image = models.ImageField(upload_to=upload_image_path_gallery,verbose_name="تصویر")

    def __str__(self):
        return self.product.title
    
    class Meta:
        verbose_name = 'گالری محصول'
        verbose_name_plural = 'گالری محصولات' 