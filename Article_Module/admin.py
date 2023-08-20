from django.contrib import admin
from .models import ArticleCategory,Article,ArticleComment,ArticleVisit

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title','url_title','parent','is_active']
    list_editable = ['url_title','parent','is_active']
admin.site.register(ArticleCategory,ArticleCategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','is_active']
    list_editable = ['is_active']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(Article,ArticleAdmin)

class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ['article','parent','user','create_date','inspection']
    list_editable = ['inspection']

admin.site.register(ArticleComment,ArticleCommentAdmin)


class ArticleVisitAdmin(admin.ModelAdmin):
    list_display = ['article','user','ip']

admin.site.register(ArticleVisit,ArticleVisitAdmin)