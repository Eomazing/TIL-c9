from django.urls import path
from . import views
# .은 현재폴더를 의미 함 => 서로 참조를 하기 위함

urlpatterns = [
    path('', views.index),
]