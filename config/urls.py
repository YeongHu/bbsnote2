"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include   #3.0에 include 도입
from bbsnote import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('bbsnote/', views.index), ↓아래와 같이 변경
    path('bbsnote/', include('bbsnote.urls')), #url 정보분리 : bbsnote의 url 정보를 urls.py 에 넣어서 url정보가 섞이는 것을 방지
    path('common/', include('common.urls')),
    path('',views.index, name='index'), #아무값도 넘어오지 않으면 이동
]
