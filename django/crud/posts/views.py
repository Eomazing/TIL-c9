from django.shortcuts import render
from .models import Post
# 현재폴더 안의 models 파일의 Post를 import 한다

# Create your views here.
# views.py -> urls.py -> templates
def new(request):
    return render(request, 'new.html')
    
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    # GET 은 throw.html 의 method get을 의미함 / get은 딕셔너리 함수 get
    
    # DB INSERT
    post = Post(title=title, content=content)
    post.save()
    
    return render(request, 'create.html')
    
def index(request):
    # All Post
    posts = Post.objects.all()
    
    return render(request, 'index.html', {'posts':posts})