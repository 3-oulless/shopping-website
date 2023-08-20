from django.db import models
from django.urls import reverse
from Account_Modul.models import User

class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory',on_delete=models.CASCADE,null=True,blank=True,verbose_name="دسته بندی والد",related_name="parents")
    title = models.CharField(max_length=200,verbose_name="عنوان دسته بندی")
    url_title = models.CharField(max_length=300,unique=True,verbose_name="عنوان در url")
    is_active = models.BooleanField(default=True,verbose_name="فعال یا غیر فعال")

    class Meta:
        verbose_name = "دسته بندی مقاله"
        verbose_name_plural = "دسته بندی مقاله ها"

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=300,verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=400,db_index=True,allow_unicode=True,verbose_name="عنوان در url")
    image = models.ImageField(upload_to='Article/',verbose_name="نصویر مقاله")
    short_description = models.TextField(verbose_name="نوضیحات کوتاه")
    text = models.TextField(verbose_name="متن مقاله")
    date_create = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True,verbose_name="فعال/غیر فعال")
    selected_categories = models.ManyToManyField(ArticleCategory,verbose_name="دسته بندی ها")
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,verbose_name="نویسنده",editable=False)
    visit_count = models.IntegerField(null=True,blank=True,default=0)

    def get_absolute_url(self):
        return reverse('article:articles_detail',args=[self.id,self.slug])

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
    
    def __str__(self):
        return self.title

class ArticleComment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.DO_NOTHING,verbose_name="مقاله")
    parent = models.ForeignKey('ArticleComment',null=True,blank=True,on_delete=models.DO_NOTHING,verbose_name="والد",related_name="article_parent")
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name="کاربر")
    create_date = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ثبت")
    text = models.TextField(verbose_name="متن نظر")
    inspection = models.BooleanField(default=True,verbose_name="بازرسی")

    class Meta:
        verbose_name = "نظر مقاله"
        verbose_name_plural = "نظرات مقاله"
    
    def __str__(self):
        return f'{self.article.title} - {self.create_date} - {self.id}'

    
class ArticleVisit(models.Model):
    article = models.ForeignKey(Article,on_delete=models.DO_NOTHING,verbose_name="نام محصول")
    ip = models.CharField(max_length=30,verbose_name='آپی کاربر')
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True,verbose_name="کاربر")

    class Meta:
        verbose_name = 'بازدید مقاله'
        verbose_name_plural = 'بازدید مقاله' 

    
    def __str__(self):
        return f'{self.article.title}-{self.ip}'