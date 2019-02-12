from django.shortcuts import render, redirect
from .models import Post, Comment
# 현재폴더 안의 models 파일의 Post를 import 한다
from django.contrib.auth.decorators import login_required

# Create your views here.
# views.py -> urls.py -> templates
@login_required # @~ :decorator, python 문법. parameter로, 아래의 함수 자체를 인자로 받아 넘겨준다.
def new(request):
    if request.method == 'POST':
        # create
        title = request.POST.get('title')
        content = request.POST.get('content')
        # GET 은 throw.html 의 method get을 의미함 / get은 딕셔너리 함수 get
        image = request.FILES.get('image')
    
        # DB INSERT
        post = Post(title=title, content=content, image=image)
        post.save()
        # 새로 생성된 페이지의 id 값
        return redirect('posts:detail', post.pk)
    else:
        return render(request, 'new.html')

    
    
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
    if request.method == 'POST':
        # 삭제하는 코드
        post = Post.objects.get(pk=post_id)
        post.delete()
        return redirect('posts:list')
    else:
        return render(request, 'delete.html')
    
def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        # update
        post.title = request.POST.get('title') # 값을 임의로 수정할 수 있음
        post.content = request.POST.get('content')
        post.save() # 값을 변경 완료하려면 반드시 입력
        
        return redirect('posts:detail', post.pk)
    else:
        #edit
        return render(request, 'edit.html', {'post':post}) # edit page에서 post 사용가능 하도록
    
    
    
def comments_create(request, post_id):
    # 댓글을 달 게시물 정보
    post = Post.objects.get(pk=post_id)
    
    # 작성할(form에서 넘어온) 댓글 내용
    content = request.POST.get('content')
    
    # 댓글 생성 및 저장
    comment = Comment(post=post, content=content)
    comment.save()
    
    return redirect('posts:detail', post.pk)
    
    # 삭제를 하고 요청을 처리해주기 때문에 render 대신 redirect 사용.
def comments_delete(request, post_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect('posts:detail', post_id)