from django.contrib import admin
from .models import Order,OrderDetail

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','user','total_invoice','tracking_code','payment_date','is_paid']
    search_fields = ['tracking_code']

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderDetail)





