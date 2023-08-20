from django.db import models

class ContactUs(models.Model):
    full_name = models.CharField(max_length=500,verbose_name="نام و نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    title = models.CharField(max_length=500,verbose_name="عنوان")
    message = models.TextField(verbose_name="متن تماس با ما")
    creat_date = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد")
    response = models.TextField(verbose_name="پاسخ ادمین",null=True,blank=True)
    is_read_by_admin = models.BooleanField(verbose_name="خوانده شده/نشده",default=False)
    
    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "لیست تماس با ما"

    def __str__(self):
        return f'{self.title} - {self.full_name}'
 