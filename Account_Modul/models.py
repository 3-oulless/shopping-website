import datetime
import os
import random
from django.db import models
from django.contrib.auth.models import AbstractUser


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    BASE_LIST = '0123456789abcdefghijklmnopqrstuvwxyz'
    new_name = ''.join(random.choices(BASE_LIST, k=10))
    name,ext = get_filename_ext(filename)
    x = datetime.datetime.now()
    final_name = f"Account/{x.year}/{x.month}/{x.day}/{new_name}{ext}"
    return final_name

class User(AbstractUser):
    avatar = models.ImageField(upload_to=upload_image_path,null=True,blank=True,verbose_name="تصویر آواتار")
    email_active_code = models.CharField(max_length=100)
    about_user = models.TextField(null=True,blank=True,verbose_name="درباره شخص")
    address = models.TextField(null=True,blank=True,verbose_name="آدرس")
    postalـcode = models.CharField(max_length=20,null=True,blank=True,verbose_name="کد پستی")
    phone = models.CharField(max_length=20,null=True,blank=True,verbose_name='موبایل')

    instagram_account = models.CharField(max_length=300,null=True,blank=True,verbose_name="اکانت اینستاگرام")
    twitter_account = models.CharField(max_length=300,null=True,blank=True,verbose_name="اکانت توییتر")
    facbook_account = models.CharField(max_length=300,null=True,blank=True,verbose_name="اکانت فیسبوک")
    linkedin_account = models.CharField(max_length=300,null=True,blank=True,verbose_name="اکانت لینکدین")


    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"
    
    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.username

class Verify_Code(models.Model):
    user = models.ForeignKey(User,verbose_name="کاربر",on_delete=models.DO_NOTHING)
    code = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.code}'