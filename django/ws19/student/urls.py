from django.urls import path
from . import views
# .은 현재폴더를 의미 함 => 서로 참조를 하기 위함

urlpatterns = [
    path('<int:student_id>/edit/', views.edit),
    path('<int:student_id>/update/', views.update),
    path('<int:student_id>/delete/', views.delete),
    path('<int:student_id>/', views.detail),
    path('create/', views.create),
    path('new/', views.new),
    path('', views.index),
]