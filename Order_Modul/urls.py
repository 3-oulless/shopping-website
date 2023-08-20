from django.urls import path
from .views import add_product_to_order,show_order,FinalStepOrder,ShowPaymentInformation


app_name = 'order'

urlpatterns = [
    path('add-to-order',add_product_to_order,name="add_to_order"),
    path('show-order',show_order,name="show_order"),
    path('by-page/',FinalStepOrder.as_view(),name='by_page'),
    path('show-information/<pk>/<int:id>',ShowPaymentInformation.as_view(),name='ShowPaymentInformation')
]