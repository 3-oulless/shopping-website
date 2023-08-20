from django.urls import path
from Account_Modul import views

app_name = 'account_modul'

urlpatterns = [
    path('register',views.RegisterView.as_view(),name="register"),
    path('login',views.LoginView.as_view(),name="login"),
    path('logout',views.LogotView.as_view(),name='logout'),
    path('active_code/<email_active_code>',views.ActivateAccountView.as_view(),name='active_code'),
    path('verify_code',views.Send_Code.as_view(),name='verify_code'),
    path('verify_code/change_password',views.Chanch_Password.as_view(),name='change_password'),
]