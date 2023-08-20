from django.urls import path
from Home_Modul import views

app_name = 'home_modul'

urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),

]