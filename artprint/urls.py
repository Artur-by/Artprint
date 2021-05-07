"""artprint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', artprintPage),
    path('zakaz/', zakazPage),
    path('zakaz/zakaz1', futbPage),
    path('zakaz/zakaz2', sweatPage),
    path('zakaz/zakaz3', tolstPage),
    path('zakaz/zakaz4', apronPage),
    path('zakaz/zakaz5', shopperPage),
    path('zakaz/zakaz6', pillowPage),
    path('zakaz/zakaz7', puzzlesPage),
    path('zakaz/zakaz8', photoPage),
    path('zakaz/zakaz9', glassPage),
    path('zakaz/zakaz10', magnitPage),
]
