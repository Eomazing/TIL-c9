from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post

# Create your views here.
def list(request):
    # models.py에 작성한 class Post의 모든 정보를 가지고 온다.
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts':posts})

# 첫번째 함수 인자로는 request가 온다.
def create(request):
    # POST 요청이라면 실제 DB에 data를 쓴다.
    if request.method == 'POST':
        # 입력한 data가 request.POST에 있기때문에 같이 실린다.
        post_form = PostForm(request.POST, request.FILES) # image 설정 후 FILES 추가
        # 들어온 data가 유효한 값인지 확인하고,
        if post_form.is_valid():
            # 저장한다.
            post_form.save()
            # 저장되어 있는지 확인하는 페이지(list:만들 예정인 페이지)
            return redirect('posts:list')
    else:
        post_form = PostForm()
    return render(request, 'posts/create.html', {'post_form': post_form})

# 게시글 업데이트    
def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # method가 POST인지 GET인지 구분해서 작동하게 만들어 준다.
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    else:
        post_form = PostForm(instance=post) # 키워드 parameter로 가져오게 되면 PostForm에 담겨서 보여진다.
    return render(request, 'posts/create.html', {'post_form': post_form})

# 게시글을 삭제하기 
def delete(request, post_id): # 추가적인 parameter 필요
    # 삭제할 특정 변수를 가져오기
    # post = Post.objects.get(id=post_id) # (pk=post_id) 동일한 결과
    # error를 발생시키지 않고 id가 없다는 것을 알려주므로 사용자 친화적
    post = get_object_or_404(Post, id=post_id) # 첫번째 인자 Post 모델
    post.delete() # method이기 때문에 delete뒤에는 ()가 필요함
    return redirect('posts:list')
    