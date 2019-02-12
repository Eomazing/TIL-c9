from django.urls import path
from . import views
# .은 현재폴더를 의미 함 => 서로 참조를 하기 위함

app_name = 'posts'

urlpatterns = [
    # path('naver/<str:q>/', views.naver),
    path('', views.index, name='list'), # GET
    path('new/', views.new, name='new'), # GET(new)
    # path('create/', views.create, name='create'), # POST(create)
    path('<int:post_id>/', views.detail, name='detail'), # GET
    path('<int:post_id>/delete/', views.delete, name='delete'), # GET(confirm), POST(delete)
    path('<int:post_id>/edit/', views.edit, name='edit'), # GET(edit), POST(update)
    # path('<int:post_id>/update/', views.update, name='update'),
    
    path('<int:post_id>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete'),
]
