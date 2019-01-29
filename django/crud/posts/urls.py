from django.urls import path
from . import views
# .은 현재폴더를 의미 함 => 서로 참조를 하기 위함

urlpatterns = [
    # path('naver/<str:q>/', views.naver),
    path('', views.index),
    path('create/', views.create),
    path('new/', views.new),
    path('<int:post_id>/', views.detail),
    path('<int:post_id>/delete/', views.delete),
    path('<int:post_id>/edit/', views.edit),
    path('<int:post_id>/update/', views.update),
]
