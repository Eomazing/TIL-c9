from django.urls import path
from . import views
# .은 현재폴더를 의미 함 => 서로 참조를 하기 위함

app_name = 'posts'

urlpatterns = [
    # path('naver/<str:q>/', views.naver),
    path('', views.index, name='list'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/update/', views.update, name='update'),
]
