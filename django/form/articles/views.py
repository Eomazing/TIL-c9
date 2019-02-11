from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleModelForm

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
        if form.is_valid(): # 지정된 값에 부합하는 데이터가 오면 True
            article = form.save()
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article(title=title, content=content)
            # article.save()
            # 위 두 줄을 아래 한 줄로 만들어줌. 동일.
            # article = Article.objects.create(title=title, content=content)
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleModelForm()
    
    return render(request, 'form.html', {'form':form})
        
def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'detail.html', {'article':article})
    
def update(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, instance=article)
        if form.is_valid(): # 지정된 값에 부합하는 데이터가 오면 True
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleModelForm(instance=article) # 수정할 때, 이전 입력값을 보여주기 위함.
        
    return render(request, 'form.html', {'form':form})