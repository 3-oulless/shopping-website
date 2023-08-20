from django.contrib import admin
from .models import Site_Setting,Social_Network_Site,FooterLink,FooterLinkBox,Slider,Employee,Site_Banner

admin.site.register(Site_Setting)
admin.site.register(Social_Network_Site)
admin.site.register(FooterLink)
admin.site.register(FooterLinkBox)


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title','url','is_active']
admin.site.register(Slider,SliderAdmin)



class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_name','employee_position','employee_recruitment_date','employee_alredy']
    list_editable = ['employee_alredy']
admin.site.register(Employee,EmployeeAdmin)



class Site_BannerAdmin(admin.ModelAdmin):
    list_display = ['title','url','position','is_active']
    list_editable = ['position','is_active']
admin.site.register(Site_Banner,Site_BannerAdmin)