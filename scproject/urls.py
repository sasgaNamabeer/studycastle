"""scproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import scapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',scapp.views.index, name="home"),
    path('blog/',scapp.views.blog, name="blog"),
    path('contact/',scapp.views.contact, name="contact"),
    path('services/',scapp.views.services, name="services.html"),
    path('blog-single/',scapp.views.blogsingle, name="blogsingle"),
]