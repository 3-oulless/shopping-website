from django.contrib import admin
from .models import Product,ProductCategory,ProductTag,ProductBrand,ProductComment,ProductVisit,ProductGallery

class ProductAdmin(admin.ModelAdmin):
    list_filter = ['category','is_active']
    list_display = ['title','price','is_active','is_delete']
    list_editable = ['price','is_active']


class ProductVisitAdmin(admin.ModelAdmin):
    list_display = ['product','user','ip']

class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ['product','image']


class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ['product','parent','user','create_date','inspection']
    list_editable = ['inspection']

admin.site.register(ProductComment,ProductCommentAdmin)

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductTag)
admin.site.register(ProductBrand)
admin.site.register(ProductVisit,ProductVisitAdmin)
admin.site.register(ProductGallery,ProductGalleryAdmin)


# Register your models here.
