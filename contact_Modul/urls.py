from django.urls import path
from .views import ContactUsView

app_name = "contact-us"

urlpatterns = [
    path('',ContactUsView.as_view(),name='contact_us')
]