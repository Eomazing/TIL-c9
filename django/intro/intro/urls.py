"""intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path # 내장함수 path => views에 저장된 링크로 보내주는 역할
from pages import views # page 폴더 안에 있는 views 파일을 import 함

urlpatterns = [
    path('bootstrap/', views.bootstrap),
    path('naver/', views.naver),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('lotto/', views.lotto),
    path('hello/<str:name>/', views.hello),
    path('dinner/', views.dinner),
    path('index/', views.index), # index 주소 생성. 새로운 주소 - 위에 쌓아 올림
    path('admin/', admin.site.urls),
]
