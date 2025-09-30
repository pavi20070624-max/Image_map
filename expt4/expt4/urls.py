"""
URL configuration for expt4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from mapapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.map,name='map'),
    path('restaurant/',views.restaurant,name='restaurant'),
    path('dental/',views.dental,name='dental'),
    path('showroom/',views.showroom,name='showroom'),
    path('school/',views.school,name='school'),
    path('hospital/',views.hospital,name='hospital'),
]
