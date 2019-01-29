from django.shortcuts import render, redirect
from .models import Post
# 현재폴더 안의 models 파일의 Post를 import 한다

# Create your views here.
# views.py -> urls.py -> templates
def new(request):
    return render(request, 'new.html')
    
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # GET 은 throw.html 의 method get을 의미함 / get은 딕셔너리 함수 get
    
    # DB INSERT
    post = Post(title=title, content=content)
    post.save()
    # 새로 생성된 페이지의 id 값
    return redirect(f'/posts/{post.pk}')
    
def index(request):
    # All Post
    posts = Post.objects.all() #=> [ < >, < >, < >]
    
    return render(request, 'index.html', {'posts':posts})
    
def detail(request, post_id): # post의 id값을 넘겨 받는다
    post = Post.objects.get(pk=post_id)
    return render(request, 'detail.html', {'post': post})
    
# 외부 사이트로 요청을 보내는 redirect 작성
# def naver(request, q):
#     return redirect(f'https://search.naver.com/search.naver?query={q}')

def delete(request, post_id):
    # 삭제하는 코드
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('/posts/')
    
def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'edit.html', {'post':post}) # edit page에서 post 사용가능 하도록
    
def update(request, post_id):
    # 수정하는 코드
    post = Post.objects.get(pk=post_id)
    post.title = request.POST.get('title') # 값을 임의로 수정할 수 있음
    post.content = request.POST.get('content')
    post.save() # 값을 변경 완료하려면 반드시 입력
    
    return redirect(f'/posts/{post_id}/')