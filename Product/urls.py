from django.urls import path
from Product import views

app_name = 'products'

urlpatterns = [
    path('',views.ProductListView.as_view(),name='Product_List'),
    path('<slug>',views.DetailView.as_view(),name='example'),
    path('brand/<data>',views.Brand_Filter,name='brand_filter'),
    path('category/<data>',views.Category_Filter,name='category_filter'),
]
