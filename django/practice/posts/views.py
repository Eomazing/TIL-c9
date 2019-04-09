from django.shortcuts import render, redirect
from .models import Post

def index(request):
    posts = Post.objects.all()
    
    return render(request, 'index.html', {'posts':posts})
    
def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    
    return render(request, 'detail.html', {'post':post})
    
def delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('/posts/')
    