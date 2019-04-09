from django.urls import path
from . import views # 추가

app_name = 'posts'

urlpatterns = [
        # path(주소창에 입력될 주소, 어떤 형식으로 보여줄 것인지, 전달할 때 사용할 주소 이름),
    path('', views.list, name='list'), # list같은 경우에는 주소가 posts/를 그대로 가지기 때문에 ''비워둔다.
    path('create/', views.create, name='create'),
    path('<int:post_id>/update/', views.update, name='update'), # 어떤 게시글을 수정할지 알아야 하기 때문에 <int:post_id> 필요
    path('<int:post_id>/delete/', views.delete, name='delete'), # <들어오게 될 변수의 type:변수의 이름(views.py에서 정의한 변수와 동일)>
    ]