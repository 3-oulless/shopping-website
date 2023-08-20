from django.urls import path
from About_Us import views

app_name = "about_us"

urlpatterns = [
    path('',views.AboutUsView.as_view(),name='about_us')
]