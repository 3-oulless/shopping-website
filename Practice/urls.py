"""
URL configuration for Practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path ('',include('Home_Modul.urls',namespace='home_modul')),
    path('auth/',include('Account_Modul.urls',namespace='account_modul')),
    path('panel/',include('User_Panel_Modul.urls',namespace='panel')),
    path('contact-us/',include('contact_Modul.urls',namespace='contact-us')),
    path('product/',include('Product.urls',namespace='product')),
    path('about-us/',include('About_Us.urls',namespace='about_us')),
    path('article/',include('Article_Module.urls',namespace='article')),
    path('order/',include('Order_Modul.urls',namespace='order')),
    path('admin/', admin.site.urls),
    
]


if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)