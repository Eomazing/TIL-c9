from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import PostForm, CommentForm
from .models import Post, Comment

# Create your views here.
def list(request):
    # models.py에 작성한 class Post의 모든 정보를 가지고 온다.
    posts = Post.objects.order_by('-id').all()
    comment_form = CommentForm()
    return render(request, 'posts/list.html', {'posts':posts, 'comment_form':comment_form})

# 첫번째 함수 인자로는 request가 온다.
@login_required
def create(request):
    # POST 요청이라면 실제 DB에 data를 쓴다.
    if request.method == 'POST':
        # 입력한 data가 request.POST에 있기때문에 같이 실린다.
        post_form = PostForm(request.POST, request.FILES) # image 설정 후 FILES 추가
        # 들어온 data가 유효한 값인지 확인하고,
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            # 저장한다.
            post_form.save() # 실제 데이터베이스에 저장
            # 저장되어 있는지 확인하는 페이지(list:만들 예정인 페이지)
            return redirect('posts:list')
    else:
        post_form = PostForm()
    return render(request, 'posts/form.html', {'post_form': post_form})

# 게시글 업데이트
@login_required
def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # post user와 로그인된 user가 다르다면, list로 redirect
    if post.user != request.user:
        return redirect('posts:list')
    # method가 POST인지 GET인지 구분해서 작동하게 만들어 준다.
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    else:
        post_form = PostForm(instance=post) # 키워드 parameter로 가져오게 되면 PostForm에 담겨서 보여진다.
    return render(request, 'posts/form.html', {'post_form': post_form})

# 게시글을 삭제하기
@login_required
def delete(request, post_id): # 추가적인 parameter 필요
    # 삭제할 특정 변수를 가져오기
    # post = Post.objects.get(id=post_id) # (pk=post_id) 동일한 결과
    # error를 발생시키지 않고 id가 없다는 것을 알려주므로 사용자 친화적
    post = get_object_or_404(Post, id=post_id) # 첫번째 인자 Post 모델
    # 1번 방법
    if post.user != request.user:
        return redirect('posts:list')
    post.delete() # method이기 때문에 delete뒤에는 ()가 필요함
    # 2번 방법
    # if post.user == request.user:
    #   post.delete()
    return redirect('posts:list')

@login_required # 로그인이 되어있는지 아닌지 확인 먼저
@require_POST # POST 요청만 받는다는 의미
def comment_create(request, post_id): # post에 대한 정보를 가지고 와서 그 정보를 바탕으로 작업이 이루어 지기 때문에 post_id 필요
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_id
        comment.save()
    return redirect('posts:list')
    
@require_http_methods(['GET', 'POST'])
def comment_delete(request, post_id, comment_id): # 두 개의 variable routing이 왔기때문에 순서에 맞춰 나열(urls.py 참조)
    # 특정 댓글을 지우기 위해서는 comment_id를 이용해서 (객체를) 가지고 온다.
    comment = get_object_or_404(Comment, id=comment_id)
    
    # 댓글을 지우기 전에 검증이 필요(작성 user와 로그인 user)
    if comment.user != request.user:
        return redirect('posts:list')
        
    comment.delete()
    return redirect('posts:list')

@login_required
def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.like_users.all():
        # 2. 좋아요 취소
        post.like_users.remove(request.user)
    else:
        # 1. 좋아요
        post.like_users.add(request.user)
    return redirect('posts:list')