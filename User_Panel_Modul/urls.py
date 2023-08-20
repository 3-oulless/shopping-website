from django.urls import path
from .views import UserPanelView,EditUserInformationView,ChangePasswordView,OrdersView,OrderDetailView
from django.contrib.auth.decorators import login_required


app_name = "panel"

urlpatterns = [
    path('', login_required(UserPanelView.as_view(),login_url='account_modul:login'),name='user_panel'),
    path('edit-profile', login_required(EditUserInformationView.as_view(),login_url='account_modul:login'),name='user_panel_edit'),
    path('order/',OrdersView.as_view(),name='order'),
    path('order/<int:pk>',OrderDetailView.as_view(),name='order_detail'),
    path('edit-password', login_required(ChangePasswordView.as_view(),login_url='account_modul:login'),name='edit_password'),
]
